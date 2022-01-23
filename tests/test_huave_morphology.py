import unittest
from elotl.nahuatl.morphology import Analyser
from json import JSONEncoder
import json


class TokenEncoder(JSONEncoder):
	def default(self, o):
		return o.__dict__

class TestAnalysis(unittest.TestCase):
	analyser = Analyser()

	def test_analysis_tokenisation(self):

		inp = "tambas."
		outp = [{"wordform": "tambas", "analyses": [[[{"lemma": "mb", "pos": "VERB", "feats": {"Person": "1", "Tense": "Past", "Number": "Sing", "Subcat": "Intr"}}], 0.0]], "pos": "VERB", "lemma": "mb"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp, tokenise=True)
		outpj = json.dumps(outp, cls=TokenEncoder)
		resj = json.dumps(res, cls=TokenEncoder)
		self.assertEqual(resj, outpj)

	def test_analysis(self):

		inp = ["tambas","."]
		outp = [{"wordform": "tambas", "analyses": [[[{"lemma": "mb", "pos": "VERB", "feats": {"Person": "1", "Tense": "Past", "Number": "Sing", "Subcat": "Intr"}}], 0.0]], "pos": "VERB", "lemma": "mb"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp)
		outpj = json.dumps(outp, cls=TokenEncoder)
		resj = json.dumps(res, cls=TokenEncoder)
		self.assertEqual(resj, outpj)


if __name__ == '__main__':
	unittest.main()



