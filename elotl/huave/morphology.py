# -*- coding: UTF-8 -*-

"""
Ejemplo de uso:


	>>> from elotl.huave.morphology import Analyser
	>>> a = Analyser()
	>>> res = a.analyse('Teat tepood tambas mal wiiüd sawün win.', tokenise=True)
"""
#from elotl.huave.orthography import Normalizer as Normaliser
from elotl.utils.morphology import AnalyzerBase


class Analyser(AnalyzerBase):
	"""
	Class for returning morphological analyses in a Python-friendly format
	with UD-style POS tags and Feature=Value pairs.

	Parameters
	----------
	lang_code: str
		ISO-639-3 code for the language variety for which you want to load and use 
		the morphological analyzer.
	tokeniser: function
		A tokenisation function, if none is provided a default tokeniser, _tokenise()
		is used which is based on regular expressions.

	"""
	def __init__(self, lang_code=None, tokeniser=None):
		# This is just a temporary default until (if ever) we support multiple varieties.
		# It seems weird to require a language code if only one variety is supported
		# especially since you already imported this from `otomi`.
		if lang_code is None:
			lang_code="huv"
		super().__init__(lang_code, tokeniser)
		

# Convenience alias for Analyser to Analyzer
class Analyzer(AnalyzerBase):
	def __init__(self, lang_code=None, tokenizer=None, normalize=True):
		if lang_code is None:
			lang_code="huv"
		super().__init__(lang_code, tokenizer)
