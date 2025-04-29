# -*- coding: UTF-8 -*-

"""
Ejemplo de uso:


	>>> from elotl.maya.morphology import Analyser
	>>> a = Analyser()
	>>> res = a.analyse('Hun pʼéel kʼìin tu yaʼalah u chan pàal beyaʼ', tokenise=True)
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
	def __init__(self, tokeniser=None):
		self.tokenise = self._tokenise	
		self.lang_code = "yua"
		if tokeniser:
			self.tokenise = tokeniser
		
		with pkg_resources.path("elotl.maya.data", f"{self.lang_code}.mor.att") as p:
			_path_to_att_dir = p
		with pkg_resources.path("elotl.maya.data", f"{self.lang_code}.mor.tsv") as p:
			_path_to_tsv_dir = p

		self.analyser = ATTFST(_path_to_att_dir)
		self.convertor = elotl.utils.morphology.Convertor(_path_to_tsv_dir)

# Convenience alias for Analyser to Analyzer
Analyzer = Analyser
