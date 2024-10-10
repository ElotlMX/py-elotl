import unittest
from elotl.nahuatl.morphology import Analyser
from json import JSONEncoder
import json


class TokenEncoder(JSONEncoder):
	def default(self, o):
		return o.__dict__

class TestVariantSelection(unittest.TestCase):

	def test_unsupported_variant(self):
		init_analyser_w_abc = lambda: Analyser(lang_code="abc")
		self.assertRaises(ValueError, init_analyser_w_abc)
	
	def test_default_variant(self):
		a = Analyser()
		self.assertEqual(a.lang_code, "nhi")

class TestAnalysisWithExplicitVariantSelectionForAzz(unittest.TestCase):
	analyser = Analyser(lang_code="azz")

	def test_analysis_tokenisation(self):

		inp = "Iwki tamatisneki a n' xiwtsin."
		outp = [{"wordform": "Iwki", "analyses": [[[{"lemma": "iuki", "pos": "ADV", "feats": {}}], 0.0]], "pos": "ADV", "lemma": "iuki"}, {"wordform": "tamatisneki", "analyses": [[[{"lemma": "mati", "pos": "VERB", "feats": {"Tense": "Fut", "Number[subj]": "Sing", "Subcat": "Tran", "Person[subj]": "3", "Person[obj]": "3", "Animacy[obj]": "Inan"}}, {"lemma": "neki", "pos": "AUX", "feats": {}}], 0.0], [[{"lemma": "tamati", "pos": "VERB", "feats": {"Person[subj]": "3", "Tense": "Fut", "Number[subj]": "Sing", "Subcat": "Intr"}}, {"lemma": "neki", "pos": "AUX", "feats": {}}], 0.0]], "pos": None, "lemma": None}, {"wordform": "a", "analyses": [[[{"lemma": "a", "pos": "INTERJ", "feats": {}}], 0.0]], "pos": "INTERJ", "lemma": "a"}, {"wordform": "n", "analyses": [[[{"lemma": "in", "pos": "DET", "feats": {}}], 0.0]], "pos": "DET", "lemma": "in"}, {"wordform": "'", "analyses": [], "pos": None, "lemma": None}, {"wordform": "xiwtsin", "analyses": [[[{"lemma": "xihuit", "pos": "NOUN", "feats": {"Polite": "Form"}}], 0.0], [[{"lemma": "xihuit", "pos": "NOUN", "feats": {"Polite": "Form", "Number[subj]": "Plur", "Person[subj]": "3"}}], 0.0], [[{"lemma": "xihuit", "pos": "NOUN", "feats": {"Person[subj]": "3", "Polite": "Form", "Number[subj]": "Sing"}}], 0.0]], "pos": "NOUN", "lemma": "xihuit"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp, tokenise=True)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)

	def test_analysis(self):

		inp = ["Iwki","tamatisneki", "a", "n'", "xiwtsin","."]
		outp = [{"wordform": "Iwki", "analyses": [[[{"lemma": "iuki", "pos": "ADV", "feats": {}}], 0.0]], "pos": "ADV", "lemma": "iuki"}, {"wordform": "tamatisneki", "analyses": [[[{"lemma": "mati", "pos": "VERB", "feats": {"Tense": "Fut", "Number[subj]": "Sing", "Subcat": "Tran", "Person[subj]": "3", "Person[obj]": "3", "Animacy[obj]": "Inan"}}, {"lemma": "neki", "pos": "AUX", "feats": {}}], 0.0], [[{"lemma": "tamati", "pos": "VERB", "feats": {"Person[subj]": "3", "Tense": "Fut", "Number[subj]": "Sing", "Subcat": "Intr"}}, {"lemma": "neki", "pos": "AUX", "feats": {}}], 0.0]], "pos": None, "lemma": None}, {"wordform": "a", "analyses": [[[{"lemma": "a", "pos": "INTERJ", "feats": {}}], 0.0]], "pos": "INTERJ", "lemma": "a"}, {"wordform": "n", "analyses": [[[{"lemma": "in", "pos": "DET", "feats": {}}], 0.0]], "pos": "DET", "lemma": "in"}, {"wordform": "'", "analyses": [], "pos": None, "lemma": None}, {"wordform": "xiwtsin", "analyses": [[[{"lemma": "xihuit", "pos": "NOUN", "feats": {"Polite": "Form"}}], 0.0], [[{"lemma": "xihuit", "pos": "NOUN", "feats": {"Polite": "Form", "Number[subj]": "Plur", "Person[subj]": "3"}}], 0.0], [[{"lemma": "xihuit", "pos": "NOUN", "feats": {"Person[subj]": "3", "Polite": "Form", "Number[subj]": "Sing"}}], 0.0]], "pos": "NOUN", "lemma": "xihuit"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)




class TestAnalysisWithExplicitVariantSelection(unittest.TestCase):
	analyser = Analyser(lang_code="nhi")

	def test_analysis_tokenisation(self):

		inp = "Nomama."
		outp = [{"wordform": "Nomama", "analyses": [[[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[psor]": "1"}}], 0.0], [[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[subj]": "3", "Number[subj]": "Sing", "Person[psor]": "1"}}], 1.0]], "pos": "NOUN", "lemma": "mama"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp, tokenise=True)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)

	def test_analysis(self):

		inp = ["Nomama","."]
		outp = [{"wordform": "Nomama", "analyses": [[[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[psor]": "1"}}], 0.0], [[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[subj]": "3", "Number[subj]": "Sing", "Person[psor]": "1"}}], 1.0]], "pos": "NOUN", "lemma": "mama"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)


class TestAnalysis(unittest.TestCase):
	analyser = Analyser()

	def test_analysis_tokenisation(self):

		inp = "Nomama."
		outp = [{"wordform": "Nomama", "analyses": [[[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[psor]": "1"}}], 0.0], [[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[subj]": "3", "Number[subj]": "Sing", "Person[psor]": "1"}}], 1.0]], "pos": "NOUN", "lemma": "mama"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp, tokenise=True)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)

	def test_analysis(self):

		inp = ["Nomama","."]
		outp = [{"wordform": "Nomama", "analyses": [[[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[psor]": "1"}}], 0.0], [[{"lemma": "mama", "pos": "NOUN", "feats": {"Number[psor]": "Sing", "Person[subj]": "3", "Number[subj]": "Sing", "Person[psor]": "1"}}], 1.0]], "pos": "NOUN", "lemma": "mama"}, {"wordform": ".", "analyses": [[[{"lemma": ".", "pos": "PUNCT", "feats": {}}], 0.0]], "pos": "PUNCT", "lemma": "."}]
		res = self.analyser.analyse(inp)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)


if __name__ == '__main__':
	unittest.main()



