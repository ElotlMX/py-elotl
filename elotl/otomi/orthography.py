# -*- coding: UTF-8 -*-

# Para usar desde la línea de comandos:
#     $ python elotl/otomi/orthography.py "<texto>" -ort [inali|otq|ots|rfe]

# O, desde otro programa de Python:

#     >>> from elotl.otomi.orthography import Normalizer
#     >>> normalizer = Normalizer("otq")  # o "ots" "rfe" "inali"
#     >>> normalizer.normalize("<texto>")  # o `normalizer.to_phones("<texto>")`

from __future__ import annotations
import logging
from elotl.utils.fst.attapply import ATTFST
from elotl.otomi.config import DEFAULT_ORTOGRAPHY, AVAILABLE_ORTHOGRAPHIES

# https://docs.python.org/3/library/importlib.html?highlight=resources#module-importlib.resources
try:
    # For Python >= 3.7
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to Python < 3.7 `importlib_resources`.
    import importlib_resources as pkg_resources

# https://importlib-resources.readthedocs.io/en/latest/using.html#migrating-from-legacy
_path_to_orig_fon = pkg_resources.files("elotl.utils.fst.att.otomi").joinpath('orig-fon.att')

_ORIG_FON_FST = ATTFST(_path_to_orig_fon)
logger = logging.getLogger(__name__)


class Normalizer(object):
    """
    Class for normalizing Otomi texts to a single orthography. Currently
    supported output orthographies:
    - OTS (e.g. "kjämadi")
    - OTQ (e.g. "hämadi")
    - INALI (e.g. "jämadi")
    - RFE (e.g. "hąmadi") 

    The entry points for converting text are `.normalize(...)` and
    `.to_phones(...)`.

    Parameters
    ----------
    normalized_ort: str
        Name of the orthography to convert everything into. Must be one of
        ("inali", "otq", "ots", "rfe").
    
    log_level: str
        Desired level of logging ("error", "warn", or "debug"). If "warn" or
        "debug", a message will be produced every time the normalizer is unable
        to convert a word in the input. This can be a bit annoying, so by
        default the log level is set to "error".

    """
    def __init__(self, normalized_ort: str = "inali", log_level="error"):
        if normalized_ort is None:
            normalized_ort = DEFAULT_ORTOGRAPHY
            logger.info(f"No Otomi Ortography code provided. Defaulting to {DEFAULT_ORTOGRAPHY}")

        if not (normalized_ort in AVAILABLE_ORTHOGRAPHIES):
            logger.warning(normalized_ort + " is not a supported orthography.")
            logger.warning(f"Using '{DEFAULT_ORTOGRAPHY}' as orthography.")
            normalized_ort = DEFAULT_ORTOGRAPHY

        log_level = log_level.lower()
        if log_level == "warn":
            logger.setLevel(logging.WARN)
        elif log_level == "error":
            logger.setLevel(logging.ERROR)
        elif log_level == "debug":
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.ERROR)
            logging.error("Log level '{}' not recognized. Setting log level to"
                          " 'ERROR'.".format(log_level))

        with pkg_resources.path("elotl.utils.fst.att.otomi",
                                "fon-" + normalized_ort + ".att") as p:
            _path_to_att_dir = p

        self.norm_fst = ATTFST(_path_to_att_dir)

    def _convert(self, w: str, fst: ATTFST) -> str:
        """
        Convert an input word form to an output form using the provided ATTFST
        object. In this implementation, we assume high weights are preferred,
        so we select the last of the generated candidates.

        Parameters
        ----------
        w: str
            Input word.

        fst: ATTFST
            FST object created with attapply. This object has an `apply`
            command used to apply the fst to an input.

        Returns
        -------
        str
            The generated string with the highest weight.

        """
        w = w.lower()
        forms = list(fst.apply(w))
        if forms:
            return forms[-1][0]

    def _g2p(self, w):
        """
        Converts an input word to a sequence of phonemes using an FST defined
        in elotl/otomi/fst/lexc/orig-fon.lexc. FIX: THIS COMMENT IS WRONG (SAME IN NAHUATL/ORTOGRAHPY)
        """
        return self._convert(w, _ORIG_FON_FST)

    def _normalize_word(self, original_word: str) -> tuple[str, str]:
        """
        Convert an input word from 'any' orthography into a normalized
        orthography (currently OTQ, INALI, OTS, and RFE). Since this process
        requires first converting the input to a pseudo-phonemic
        representation, we return both the phonemic and normalized forms.

        Parameters
        ----------
        original_word: str
            Input word form, in theory in any mixture of common Otomi
            orthographies.

        Returns
        -------
        Tuple
            Phonemic, Normalized forms of the string.

        """
        w = original_word.lower()

        fon = self._g2p(w)
        if fon is None:
            logger.warn("Unable to convert word '{}' to phonemes."
                        .format(w))
            return w, w

        normed = self._convert(fon, self.norm_fst)
        if normed is None:
            logger.warn("Unable to convert word '{}'.from phonemes to "
                        "normalized orthography.".format(fon))
            return fon, w

        return fon, normed

    @staticmethod
    def _tokenize(s):
        return s.split()

    def to_phones(self, text: str, overrides: dict[str, str] = None) -> str:
        """
        Convert a non-normalized Otomi text into approximate/pseudo IPA. 
        Conversion happens at the word-level after tokenizing on whitespace.

        Parameters
        ----------
        text: str
            Input text. It can be from any of a number of possible Otomi
            orthographies (the system attempts to handle many of the graphic
            variations observed in diverse Otomi texts).

        overrides: dict
            A dictionary of hard-coded normalizations. If an input word
            (lowered) is contained in the dictionary, we will use the form it
            maps to instead of applying the FST on it.

        Returns
        -------
        str
            Whitespace-joined words converted to approximate phonemic
            representation.

        """
        overrides = overrides if overrides is not None else {}
        fon = []
        for token in self._tokenize(text):
            if token in overrides:
                t_fon = overrides[token.lower()]
            t_fon = self._g2p(token)
            if t_fon is None:
                logger.warn("Unable to convert word '{}' to phonemes."
                            .format(token))
                fon.append(token)
                continue
            fon.append(t_fon)

        return " ".join(fon)

    def normalize(self, text: str, overrides: dict[str, str] = None) -> str:
        """
        Convert a non-normalized Otomi text into normalized orthography.
        Depending on the value used when initializing this class, the
        normalized orthography is OTQ, INALI, OTS, and RFE. Conversion happens
        at the word-level after tokenizing on whitespace.

        Parameters
        ----------
        text: str
            Input text. It can be from any of a number of possible Otomi
            orthographies (the system attempts to handle many of the graphic
            variations observed in diverse Otomi texts).

        overrides: dict
            A dictionary of hard-coded normalizations. If an input word
            (lowered) is contained in the dictionary, we will use the form it
            maps to instead of applying the FST on it.

        Returns
        -------
        str
            Whitespace-joined words converted to normalized orthography.

        """
        overrides = overrides if overrides is not None else {}
        norm = []
        for token in self._tokenize(text):
            if token in overrides:
                norm.append(overrides[token])
                continue
            _, t_norm = self._normalize_word(token)

            norm.append(t_norm)

        return " ".join(norm)
