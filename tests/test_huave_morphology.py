import unittest
from elotl.huave.morphology import Analyser
from json import JSONEncoder
import json


class TokenEncoder(JSONEncoder):
	def default(self, o):
		return o.__dict__

class TestAnalysis(unittest.TestCase):
	analyser = Analyser()

	def test_analysis_tokenisation(self):
		self.maxDiff=None

		inp = "tambas."
		outp = [{"wordform": "tambas", "analyses": [[[{"lemma": "mb", "pos": "VERB", "feats": {"Person": "1", "Tense": "Past", "Number": "Sing", "Subcat": "Intr"}}], 0.0]], "pos": "VERB", "lemma": "mb"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp, tokenise=True)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)

	def test_analysis(self):

		inp = ["tambas","."]
		outp = [{"wordform": "tambas", "analyses": [[[{"lemma": "mb", "pos": "VERB", "feats": {"Person": "1", "Tense": "Past", "Number": "Sing", "Subcat": "Intr"}}], 0.0]], "pos": "VERB", "lemma": "mb"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)


if __name__ == '__main__':
	unittest.main()



