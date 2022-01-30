import unittest
from elotl.otomi.morphology import Analyser
from json import JSONEncoder
import json


class TokenEncoder(JSONEncoder):
	def default(self, o):
		return o.__dict__

class TestAnalysis(unittest.TestCase):
	analyser = Analyser()

	def test_analysis_tokenisation(self):
		self.maxDiff=None

		inp = "dada."
		outp = [{"wordform": "dada", "analyses": [[[{"lemma": "dada", "pos": "NOUN", "feats": {}}], 0.0], [[{"lemma": "da", "pos": "AUX", "feats": {"Tense": "Fut", "Person[subj]": "3"}}, {"lemma": "t\u00e4", "pos": "VERB", "feats": {"Subcat": "Intr"}}], 0.0]], "pos": "NOUN", "lemma": "dada"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp, tokenise=True)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)

	def test_analysis(self):

		inp = ["dada", "."]
		outp = [{"wordform": "dada", "analyses": [[[{"lemma": "dada", "pos": "NOUN", "feats": {}}], 0.0], [[{"lemma": "da", "pos": "AUX", "feats": {"Tense": "Fut", "Person[subj]": "3"}}, {"lemma": "t\u00e4", "pos": "VERB", "feats": {"Subcat": "Intr"}}], 0.0]], "pos": "NOUN", "lemma": "dada"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)


if __name__ == '__main__':
	unittest.main()



