# -*- coding: UTF-8 -*-

"""
Ejemplo de uso:


	>>> from elotl.nahuatl.morphology import Analyser
	>>> a = Analyser()
	>>> res = a.analyse('“Amo quen ximati, teh xiyo in escuela.', tokenise=True)
"""
import logging
from elotl.nahuatl.orthography import Normalizer as Normaliser
from elotl.utils.morphology import Analyzer as GenericElotlAnalyzer

logger = logging.getLogger(__name__)


class Analyser(GenericElotlAnalyzer):
	"""
	Class for returning morphological analyses in a Python-friendly format
	with UD-style POS tags and Feature=Value pairs.

	Parameters
	----------
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
	def __init__(self, lang_code, tokenizer=None, normalize=True):
		super().__init__(lang_code, tokenizer)
		if normalize is True:
			self.normaliser = Normaliser("ack")

# Convenience alias for Analyser to Analyzer
Analyzer = Analyser
