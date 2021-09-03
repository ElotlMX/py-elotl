# -*- coding: UTF-8 -*-

# Para usar desde la línea de comandos:
#     $ python elotl/nahuatl/orthography.py "<texto>" -ort [sep-u-j|sep-w-h|ack]

# O, desde otro programa de Python:

#     >>> from elotl.nahuatl.orthography import Normalizer
#     >>> normalizer = Normalizer("sep-u-j")  # o "sep-w-h" "ack"
#     >>> normalizer.normalize("<texto>")  # o `normalizer.to_phones("<texto>")`

from __future__ import annotations
#import argparse
#from pathlib import Path

from elotl.utils.fst.attapply import ATTFST

# https://docs.python.org/3/library/importlib.html?highlight=resources#module-importlib.resources
try:
    # For Python >= 3.7
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to Python < 3.7 `importlib_resources`.
    import importlib_resources as pkg_resources

# https://stackoverflow.com/a/58520692
with pkg_resources.path("elotl.utils.fst.att", "orig-fon.att") as p:
    _path_to_orig_fon = p

_ORIG_FON_FST = ATTFST(_path_to_orig_fon)
_available_orthographies = ['sep-u-j', 'sep-w-h', 'ack']

class Normalizer(object):
    """
    Class for normalizing Nahuatl texts to a single orthography. Currently
    supported output orthographies:
    - SEP-U-J (e.g. "tiualaske")
    - SEP-W-H
    - ACK (e.g. "tihualazque").

    The entry points for converting text are `.normalize(...)` and
    `.to_phones(...)`.

    Parameters
    ----------
    normalized_ort: str
        Name of the orthography to convert everything into. Must be one of
        ("sep-u-j", "sep-w-h", "ack").

    """
    def __init__(self, normalized_ort: str = "sep-u-j"):
        if not (normalized_ort in _available_orthographies):
            print(normalized_ort + " is not a supported orthography.")
            print("Using sep-u-j as orthography.")
            normalized_ort = "sep-u-j"

        with pkg_resources.path("elotl.utils.fst.att", "fon-" + normalized_ort + ".att") as p:
            _path_to_att_dir = p

        self.norm_fst = ATTFST(_path_to_att_dir)

    def _convert(self, w: str, fst: ATTFST) -> str:
        """
        Convert an input word form to an output form using the provided ATTFST
        object. In this implementation, we assume high weights are preferred,
        so we select the last of the generated candidates.SEP

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
        in elotl/nahuatl/fst/lexc/orig-fon.lexc.
        """
        return self._convert(w, _ORIG_FON_FST)

    def _normalize_word(self, original_word: str) -> tuple[str, str]:
        """
        Convert an input word from 'any' orthography into a normalized
        orthography (currently SEP-U-J, SEP-W-H and ACK). Since this process
        requires first converting the input to a pseudo-phonemic
        representation, we return both the phonemic and normalized forms.

        Parameters
        ----------
        original_word: str
            Input word form, in theory in any mixture of common Nahuatl
            orthographies.

        Returns
        -------
        Tuple
            Phonemic, Normalized forms of the string.

        """
        w = original_word.lower()

        fon = self._g2p(w)
        if fon is None:
            # TODO: log this as a warning instead of printing to stdout.
            print("Unable to convert word '{}' to phonemes."
                  .format(w))
            return w, w

        normed = self._convert(fon, self.norm_fst)
        if normed is None:
            # TODO: log this as a warning instead of printing to stdout.
            print("Unable to convert word '{}'.from phonemes to "
                  "normalized orthography.".format(fon))
            return fon, w

        return fon, normed

    @staticmethod
    def _tokenize(s):
        return s.split()

    def to_phones(self, text: str, overrides: dict[str, str] = None) -> str:
        """
        Convert a non-normalized Nahuatl text into approximate/pseudo IPA.
        Conversion happens at the word-level after tokenizing on whitespace.

        Parameters
        ----------
        text: str
            Input text. It can be from any of a number of possible Nahuatl
            orthographies (the system attempts to handle many of the graphic
            variations observed in diverse Nahuatl texts).

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
            fon.append(t_fon)

        return " ".join(fon)

    def normalize(self, text: str, overrides: dict[str, str] = None) -> str:
        """
        Convert a non-normalized Nahuatl text into normalized orthography.
        Depending on the value used when initializing this class, the
        normalized orthography is SEP-U-J, SEP-W-H or ACK. Conversion happens at the
        word-level after tokenizing on whitespace.

        Parameters
        ----------
        text: str
            Input text. It can be from any of a number of possible Nahuatl
            orthographies (the system attempts to handle many of the graphic
            variations observed in diverse Nahuatl texts).

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


#if __name__ == "__main__":
#    argparser = argparse.ArgumentParser()
#    argparser.add_argument("texto")
#    argparser.add_argument("--ortografia_preferida", "-ort",
#                           choices=["sep", "ack"], default="sep")

#    args = argparser.parse_args()
#    n = Normalizer(output_ort=args.ortografia_preferida)
#    print(n.normalize(args.texto))
