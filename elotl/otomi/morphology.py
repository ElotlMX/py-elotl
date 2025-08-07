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


logger = logging.getLogger(__name__)

class Analyser(AnalyzerBase):
	def __init__(self, lang_code=None, tokeniser=None, normalise=False):
		# This is just a temporary default until (if ever) we support multiple varieties.
		# It seems weird to require a language code if only one variety is supported
		# especially since you already imported this from `otomi`.
		if lang_code is None:
			lang_code="ote"
		super().__init__(lang_code, tokeniser)

		if normalise is True:
			self.normaliser = Normaliser("inali") # todo: verify that this orthography is the most compatible with the morphological analyzer.


# Convenience alias for Analyser to Analyzer
class Analyzer(AnalyzerBase):
	def __init__(self, lang_code=None, tokenizer=None, normalize=True):
		if lang_code is None:
			lang_code="ote"
		super().__init__(lang_code, tokenizer)
