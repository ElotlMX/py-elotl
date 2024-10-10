# -*- coding: UTF-8 -*-

"""
Ejemplo de uso:


	>>> from elotl.nahuatl.morphology import Analyser
	>>> a = Analyser()
	>>> res = a.analyse('“Amo quen ximati, teh xiyo in escuela.', tokenise=True)
"""
import logging
from elotl.utils.fst.attapply import ATTFST
from elotl.nahuatl.orthography import Normalizer as Normaliser
import elotl.utils.morphology
from elotl.nahuatl.config import SUPPORTED_LANG_CODES, DEFAULT_LANG_CODE

try:
	# For Python >= 3.7
	import importlib.resources as pkg_resources
except ImportError:
	# Try backported to Python < 3.7 `importlib_resources`.
	import importlib_resources as pkg_resources

logger = logging.getLogger(__name__)


class Analyser(elotl.utils.morphology.Analyser):
	"""
	Class for returning morphological analyses in a Python-friendly format
	with UD-style POS tags and Feature=Value pairs.

	Parameters
	----------
	tokeniser: function
		A tokenisation function, if none is provided a default tokeniser, _tokenise()
		is used which is based on regular expressions.

	"""
	def __init__(self, tokeniser=None, lang_code=None):
		self.tokenise = self._tokenise

		if lang_code is None:
			self.lang_code = DEFAULT_LANG_CODE
			logger.info("No Nahuatl variant language code provided. "
			            "Defaulting to `nhi`.")
		else:
			if lang_code not in SUPPORTED_LANG_CODES:
				logger.error("Unsupported language variant specified.")
				raise ValueError(f"Unsupported lang code for Nahuatl: "
								 f"{lang_code}")
			else:
				self.lang_code = lang_code
		if tokeniser:
			self.tokenise = tokeniser

		_path_to_att_dir = pkg_resources.files("elotl.nahuatl.data").joinpath(f"{self.lang_code}.mor.att")
		_path_to_tsv_dir = pkg_resources.files("elotl.nahuatl.data").joinpath(f"{self.lang_code}.mor.tsv")

		self.analyser = ATTFST(_path_to_att_dir)
		self.convertor = elotl.utils.morphology.Convertor(_path_to_tsv_dir)
		self.normaliser = Normaliser("ack")

# Convenience alias for Analyser to Analyzer
Analyzer = Analyser
