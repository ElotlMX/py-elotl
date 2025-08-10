# -*- coding: UTF-8 -*-

"""
Ejemplo de uso:

	>>> from elotl.otomi.morphology import Analyser
	>>> a = Analyser()
	>>> res = a.analyse('Mä ga ze̱ngua mä dada habu̱ bí ʼbu̱i', tokenise=True)
"""
import logging
from elotl.otomi.orthography import Normalizer as Normaliser
from elotl.utils.morphology import AnalyzerBase
from elotl.otomi.config import SUPPORTED_LANG_CODES, DEFAULT_LANG_CODE
from typing import Callable, Optional

logger = logging.getLogger(__name__)

class Analyser(AnalyzerBase):
	def __init__(self, lang_code: Optional[str] = None, tokeniser: Optional[Callable] = None, normalise: bool = False):
		"""
		Parameters
		----------
		lang_code: str or None
			ISO-639-3 code for the language variety for which you want to load and use 
			the morphological analyzer. This is just a temporary default until (if ever) 
			we support multiple varieties. It seems weird to require a language code if 
			only one variety is supported especially since you already imported this 
			from `otomi`.
		tokeniser: function
			A tokenisation function, if none is provided a default tokeniser, _tokenise()
			is used which is based on regular expressions.
		normalize: bool
			Whether of not to perform orthographic normalization on the input prior to
			passing it to the analyzer. Each language's analyzer should have its own
			default target normalized orthography (depending on the orthogaphy used in the analyzer).
			In some cases this may be beneficial. Often, though, it may not be necessary,
			since most of the morphological analyzers, at least those that we currently leverage
			from the apertium project, were built with a "spellrelax" component that enables
			flexible input orthography.
		"""
		if lang_code is None:
			lang_code="ote"
		super().__init__(lang_code, tokeniser)

		if normalise:
			self.normaliser = Normaliser("inali") # todo: verify that this orthography is the most compatible with the morphological analyzer.


# Convenience alias for Analyser to Analyzer
class Analyzer(AnalyzerBase):
	def __init__(self, lang_code: Optional[str] = None, tokenizer: Optional[Callable] = None, normalize: bool = False):
		if lang_code is None:
			lang_code="ote"
		if normalize:
			self.normaliser = Normaliser("inali") # todo: verify that this orthography is the most compatible with the morphological analyzer.

		super().__init__(lang_code, tokenizer)
