# -*- coding: UTF-8 -*-

"""
Ejemplo de uso:


	>>> from elotl.huave.morphology import Analyser
	>>> a = Analyser()
	>>> res = a.analyse('Teat tepood tambas mal wiiüd sawün win.', tokenise=True)
"""

from elotl.utils.fst.attapply import ATTFST
#from elotl.huave.orthography import Normalizer as Normaliser
import elotl.utils.morphology

try:
	# For Python >= 3.7
	import importlib.resources as pkg_resources
except ImportError:
	# Try backported to Python < 3.7 `importlib_resources`.
	import importlib_resources as pkg_resources

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

		if tokeniser:
			self.tokenise = tokeniser

		with pkg_resources.path("elotl.huave.data", "huv.mor.att") as p:
			_path_to_att_dir = p
		with pkg_resources.path("elotl.huave.data", "huv.mor.tsv") as p:
			_path_to_tsv_dir = p

		self.analyser = ATTFST(_path_to_att_dir)
		self.convertor = elotl.utils.morphology.Convertor(_path_to_tsv_dir)
		#self.normaliser = Normaliser("ack")
		self.normaliser = None

# Convenience alias for Analyser to Analyzer
Analyzer = Analyser
