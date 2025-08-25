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
	

class TestAnalysisAzz(unittest.TestCase):
	analyser = Analyser("azz")

	def test_analysis_tokenisation(self):

		inp = "Iwki tamatisneki a n' xiwtsin."
		outp = [{'analyses': [[[{'feats': {}, 'lemma': 'iuki', 'pos': 'ADV'}], 0.0]], 'lemma': 'iuki', 'pos': 'ADV', 'wordform': 'Iwki'}, {'analyses': [[[{'feats': {'Animacy[obj]': 'Inan', 'Number[subj]': 'Sing', 'Person[obj]': '3', 'Person[subj]': '3', 'Subcat': 'Tran', 'Tense': 'Fut'}, 'lemma': 'mati', 'pos': 'VERB'}, {'feats': {}, 'lemma': 'neki', 'pos': 'AUX'}], 0.0], [[{'feats': {'Number[subj]': 'Sing', 'Person[subj]': '3', 'Subcat': 'Intr', 'Tense': 'Fut'}, 'lemma': 'tamati', 'pos': 'VERB'}, {'feats': {}, 'lemma': 'neki', 'pos': 'AUX'}], 0.0]], 'lemma': None, 'pos': None, 'wordform': 'tamatisneki'}, {'analyses': [[[{'feats': {}, 'lemma': 'a', 'pos': 'INTJ'}], 0.0]], 'lemma': 'a', 'pos': 'INTJ', 'wordform': 'a'}, {'analyses': [[[{'feats': {}, 'lemma': 'in', 'pos': 'DET'}], 0.0]], 'lemma': 'in', 'pos': 'DET', 'wordform': 'n'}, {'analyses': [], 'lemma': None, 'pos': None, 'wordform': "'"}, {'analyses': [[[{'feats': {'Polite': 'Form'}, 'lemma': 'xihuit', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Number[subj]': 'Plur', 'Person[subj]': '3', 'Polite': 'Form'}, 'lemma': 'xihuit', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Number[subj]': 'Sing', 'Person[subj]': '3', 'Polite': 'Form'}, 'lemma': 'xihuit', 'pos': 'NOUN'}], 0.0]], 'lemma': 'xihuit', 'pos': 'NOUN', 'wordform': 'xiwtsin'}, {'analyses': [[[{'feats': {}, 'lemma': '.', 'pos': 'PUNCT'}], 0.0]], 'lemma': '.', 'pos': 'PUNCT', 'wordform': '.'}]
		res = self.analyser.analyse(inp, tokenise=True)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)

	def test_analysis(self):

		inp = ["Iwki","tamatisneki", "a", "n'", "xiwtsin","."]
		outp = [{"analyses": [[[{"feats": {}, "lemma": "iuki", "pos": "ADV"}], 0.0]], "lemma": "iuki", "pos": "ADV", "wordform": "Iwki"}, {"analyses": [[[{"feats": {"Animacy[obj]": "Inan", "Number[subj]": "Sing", "Person[obj]": "3", "Person[subj]": "3", "Subcat": "Tran", "Tense": "Fut"}, "lemma": "mati", "pos": "VERB"}, {"feats": {}, "lemma": "neki", "pos": "AUX"}], 0.0], [[{"feats": {"Number[subj]": "Sing", "Person[subj]": "3", "Subcat": "Intr", "Tense": "Fut"}, "lemma": "tamati", "pos": "VERB"}, {"feats": {}, "lemma": "neki", "pos": "AUX"}], 0.0]], "lemma": None, "pos": None, "wordform": "tamatisneki"}, {"analyses": [[[{"feats": {}, "lemma": "a", "pos": "INTJ"}], 0.0]], "lemma": "a", "pos": "INTJ", "wordform": "a"}, {"analyses": [[[{"feats": {}, "lemma": "nik", "pos": "X"}], 0.0], [[{"feats": {}, "lemma": "nik", "pos": "X"}], 0.0], [[{"feats": {}, "lemma": "in", "pos": "DET"}], 0.0]], "lemma": None, "pos": None, "wordform": "n\'"}, {"analyses": [[[{"feats": {"Polite": "Form"}, "lemma": "xihuit", "pos": "NOUN"}], 0.0], [[{"feats": {"Number[subj]": "Plur", "Person[subj]": "3", "Polite": "Form"}, "lemma": "xihuit", "pos": "NOUN"}], 0.0], [[{"feats": {"Number[subj]": "Sing", "Person[subj]": "3", "Polite": "Form"}, "lemma": "xihuit", "pos": "NOUN"}], 0.0]], "lemma": "xihuit", "pos": "NOUN", "wordform": "xiwtsin"}, {"analyses": [[[{"feats": {}, "lemma": ".", "pos": "PUNCT"}], 0.0]], "lemma": ".", "pos": "PUNCT", "wordform": "."}]
		res = self.analyser.analyse(inp)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)


class TestAnalysisNhi(unittest.TestCase):
	analyser = Analyser("nhi")

	def test_analysis_tokenisation(self):
		inp = "Nomama."
		outp = [{'analyses': [[[{'feats': {'Number[psor]': 'Sing', 'Person[psor]': '1'}, 'lemma': 'mama', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Foreign': 'Yes', 'Gender': 'Fem', 'Number[psor]': 'Sing', 'Person[psor]': '1'}, 'lemma': 'mama', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Gender': 'Fem', 'Number[psor]': 'Sing', 'Person[psor]': '1'}, 'lemma': 'mama', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Number[psor]': 'Sing', 'Person[psor]': '1'}, 'lemma': 'maman', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Number[psor]': 'Sing', 'Number[subj]': 'Sing', 'Person[psor]': '1', 'Person[subj]': '3'}, 'lemma': 'mama', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Foreign': 'Yes', 'Gender': 'Fem', 'Number[psor]': 'Sing', 'Number[subj]': 'Sing', 'Person[psor]': '1', 'Person[subj]': '3'}, 'lemma': 'mama', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Gender': 'Fem', 'Number[psor]': 'Sing', 'Number[subj]': 'Sing', 'Person[psor]': '1', 'Person[subj]': '3'}, 'lemma': 'mama', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Number[psor]': 'Sing', 'Number[subj]': 'Sing', 'Person[psor]': '1', 'Person[subj]': '3'}, 'lemma': 'maman', 'pos': 'NOUN'}], 0.0]], 'lemma': None, 'pos': 'NOUN', 'wordform': 'Nomama'}, {'analyses': [[[{'feats': {}, 'lemma': '.', 'pos': 'PUNCT'}], 0.0]], 'lemma': '.', 'pos': 'PUNCT', 'wordform': '.'}]
		res = self.analyser.analyse(inp, tokenise=True)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)

	def test_analysis(self):

		inp = ["Nomama","."]
		outp = [{'analyses': [[[{'feats': {'Number[psor]': 'Sing', 'Person[psor]': '1'}, 'lemma': 'mama', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Foreign': 'Yes', 'Gender': 'Fem', 'Number[psor]': 'Sing', 'Person[psor]': '1'}, 'lemma': 'mama', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Gender': 'Fem', 'Number[psor]': 'Sing', 'Person[psor]': '1'}, 'lemma': 'mama', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Number[psor]': 'Sing', 'Person[psor]': '1'}, 'lemma': 'maman', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Number[psor]': 'Sing', 'Number[subj]': 'Sing', 'Person[psor]': '1', 'Person[subj]': '3'}, 'lemma': 'mama', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Foreign': 'Yes', 'Gender': 'Fem', 'Number[psor]': 'Sing', 'Number[subj]': 'Sing', 'Person[psor]': '1', 'Person[subj]': '3'}, 'lemma': 'mama', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Gender': 'Fem', 'Number[psor]': 'Sing', 'Number[subj]': 'Sing', 'Person[psor]': '1', 'Person[subj]': '3'}, 'lemma': 'mama', 'pos': 'NOUN'}], 0.0], [[{'feats': {'Number[psor]': 'Sing', 'Number[subj]': 'Sing', 'Person[psor]': '1', 'Person[subj]': '3'}, 'lemma': 'maman', 'pos': 'NOUN'}], 0.0]], 'lemma': None, 'pos': 'NOUN', 'wordform': 'Nomama'}, {'analyses': [[[{'feats': {}, 'lemma': '.', 'pos': 'PUNCT'}], 0.0]], 'lemma': '.', 'pos': 'PUNCT', 'wordform': '.'}]
		res = self.analyser.analyse(inp)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)

class TestAnalysisNci(unittest.TestCase):
	analyser = Analyser("nci")

	def test_analysis_tokenisation(self):
		inp = "quinmictizque ynic amo quincenpopolozque"
		outp = [{'analyses': [[[{'feats': {'Number[obj]': 'Plur', 'Number[subj]': 'Plur', 'Person[obj]': '3', 'Person[subj]': '3', 'Subcat': 'Tran', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': 'mictia', 'pos': 'VERB'}], 0.0], [[{'feats': {'Number[obj]': 'Plur', 'Person[obj]': '3', 'Subcat': 'Tran', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': 'mictia', 'pos': 'VERB'}], 0.0]], 'lemma': 'mictia', 'pos': 'VERB', 'wordform': 'quinmictizque'}, {'analyses': [], 'lemma': None, 'pos': None, 'wordform': 'ynic'}, {'analyses': [[[{'feats': {}, 'lemma': 'amo', 'pos': 'ADV'}], 0.0]], 'lemma': 'amo', 'pos': 'ADV', 'wordform': 'amo'}, {'analyses': [[[{'feats': {'Number[dat]': 'Plur', 'Number[subj]': 'Plur', 'Person[dat]': '3', 'Person[subj]': '3', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': '«cen»pohpoloa', 'pos': 'VERB'}], 0.0], [[{'feats': {'Number[obj]': 'Sing', 'Number[subj]': 'Plur', 'Person[obj]': '3', 'Person[subj]': '3', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': '«cen»pohpoloa', 'pos': 'VERB'}], 0.0], [[{'feats': {'Number[obj]': 'Plur', 'Number[subj]': 'Plur', 'Person[obj]': '3', 'Person[subj]': '3', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': '«cen»pohpoloa', 'pos': 'VERB'}], 0.0], [[{'feats': {'Number[dat]': 'Plur', 'Person[dat]': '3', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': '«cen»pohpoloa', 'pos': 'VERB'}], 0.0], [[{'feats': {'Number[obj]': 'Sing', 'Person[obj]': '3', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': '«cen»pohpoloa', 'pos': 'VERB'}], 0.0], [[{'feats': {'Number[obj]': 'Plur', 'Person[obj]': '3', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': '«cen»pohpoloa', 'pos': 'VERB'}], 0.0]], 'lemma': '«cen»pohpoloa', 'pos': 'VERB', 'wordform': 'quincenpopolozque'}]
		res = self.analyser.analyse(inp, tokenise=True)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)

	def test_analysis(self):

		inp = ['quinmictizque', 'ynic', 'amo', 'quincenpopolozque']
		outp = [{'analyses': [[[{'feats': {'Number[obj]': 'Plur', 'Number[subj]': 'Plur', 'Person[obj]': '3', 'Person[subj]': '3', 'Subcat': 'Tran', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': 'mictia', 'pos': 'VERB'}], 0.0], [[{'feats': {'Number[obj]': 'Plur', 'Person[obj]': '3', 'Subcat': 'Tran', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': 'mictia', 'pos': 'VERB'}], 0.0]], 'lemma': 'mictia', 'pos': 'VERB', 'wordform': 'quinmictizque'}, {'analyses': [], 'lemma': None, 'pos': None, 'wordform': 'ynic'}, {'analyses': [[[{'feats': {}, 'lemma': 'amo', 'pos': 'ADV'}], 0.0]], 'lemma': 'amo', 'pos': 'ADV', 'wordform': 'amo'}, {'analyses': [[[{'feats': {'Number[dat]': 'Plur', 'Number[subj]': 'Plur', 'Person[dat]': '3', 'Person[subj]': '3', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': '«cen»pohpoloa', 'pos': 'VERB'}], 0.0], [[{'feats': {'Number[obj]': 'Sing', 'Number[subj]': 'Plur', 'Person[obj]': '3', 'Person[subj]': '3', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': '«cen»pohpoloa', 'pos': 'VERB'}], 0.0], [[{'feats': {'Number[obj]': 'Plur', 'Number[subj]': 'Plur', 'Person[obj]': '3', 'Person[subj]': '3', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': '«cen»pohpoloa', 'pos': 'VERB'}], 0.0], [[{'feats': {'Number[dat]': 'Plur', 'Person[dat]': '3', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': '«cen»pohpoloa', 'pos': 'VERB'}], 0.0], [[{'feats': {'Number[obj]': 'Sing', 'Person[obj]': '3', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': '«cen»pohpoloa', 'pos': 'VERB'}], 0.0], [[{'feats': {'Number[obj]': 'Plur', 'Person[obj]': '3', 'Tense': 'Fut', 'VerbForm': 'Fin'}, 'lemma': '«cen»pohpoloa', 'pos': 'VERB'}], 0.0]], 'lemma': '«cen»pohpoloa', 'pos': 'VERB', 'wordform': 'quincenpopolozque'}]
		res = self.analyser.analyse(inp)
		outpj = json.dumps(outp, cls=TokenEncoder, sort_keys=True)
		resj = json.dumps(res, cls=TokenEncoder, sort_keys=True)
		self.assertEqual(resj, outpj)


if __name__ == '__main__':
	unittest.main()



