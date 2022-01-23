import unittest
from elotl.nahuatl.morphology import Analyser
from json import JSONEncoder
import json


class TokenEncoder(JSONEncoder):
	def default(self, o):
		return o.__dict__

class TestVariantSelection(unittest.TestCase):

	def test_unsupported_variant(self):
		self.assertRaises(ValueError, Analyser("abc"))
	
	def test_default_variant(self):
		a = Analyser()
		self.assertEquals(a.lang_code, "nhi")

class TestAnalysisWithExplicitVariantSelection(unittest.TestCase):
	analyser = Analyser(lang_code="nhi")

	def test_analysis_tokenisation(self):

		inp = "Nomama."
		outp = [{"wordform": "Nomama", "analyses": [[[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[psor]": "1"}}], 0.0], [[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[subj]": "3", "Number[subj]": "Sing", "Person[psor]": "1"}}], 1.0]], "pos": "NOUN", "lemma": "mama"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp, tokenise=True)
		outpj = json.dumps(outp, cls=TokenEncoder)
		resj = json.dumps(res, cls=TokenEncoder)
		self.assertEqual(resj, outpj)

	def test_analysis(self):

		inp = ["Nomama","."]
		outp = [{"wordform": "Nomama", "analyses": [[[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[psor]": "1"}}], 0.0], [[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[subj]": "3", "Number[subj]": "Sing", "Person[psor]": "1"}}], 1.0]], "pos": "NOUN", "lemma": "mama"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp)
		outpj = json.dumps(outp, cls=TokenEncoder)
		resj = json.dumps(res, cls=TokenEncoder)
		self.assertEqual(resj, outpj)

		
class TestAnalysis(unittest.TestCase):
	analyser = Analyser()

	def test_analysis_tokenisation(self):

		inp = "Nomama."
		outp = [{"wordform": "Nomama", "analyses": [[[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[psor]": "1"}}], 0.0], [[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[subj]": "3", "Number[subj]": "Sing", "Person[psor]": "1"}}], 1.0]], "pos": "NOUN", "lemma": "mama"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp, tokenise=True)
		outpj = json.dumps(outp, cls=TokenEncoder)
		resj = json.dumps(res, cls=TokenEncoder)
		self.assertEqual(resj, outpj)

	def test_analysis(self):

		inp = ["Nomama","."]
		outp = [{"wordform": "Nomama", "analyses": [[[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[psor]": "1"}}], 0.0], [[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[subj]": "3", "Number[subj]": "Sing", "Person[psor]": "1"}}], 1.0]], "pos": "NOUN", "lemma": "mama"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp)
		outpj = json.dumps(outp, cls=TokenEncoder)
		resj = json.dumps(res, cls=TokenEncoder)
		self.assertEqual(resj, outpj)


if __name__ == '__main__':
	unittest.main()



