# -*- coding: UTF-8 -*-

# Para usar desde la línea de comandos:
#     $ python elotl/nahuatl/orthography.py "<texto>" -ort [sep|inali|ack]

# O, desde otro programa de Python:

#     >>> from elotl.nahuatl.orthography import Normalizer
#     >>> normalizer = Normalizer("sep")  # o "inali" "ack"
#     >>> normalizer.normalize("<texto>")  # o `normalizer.to_phones("<texto>")`

#from __future__ import annotations
import logging
import re 
from elotl.utils.fst.attapply import ATTFST

try:
    # For Python >= 3.7
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to Python < 3.7 `importlib_resources`.
    import importlib_resources as pkg_resources

class Token(object):
	"""
		Each analysis is formed of a weight and a sequence of words, a token may 
		contain more than one word, a word is a triple of (lemma, pos, [feat=value])
	"""
	def __init__(self, wordform, analyses = []):
		self.wordform = wordform
		self.analyses = analyses

	def __repr__(self):
		return '<Token "{0}" ({1})>'.format(self.wordform,len(self.analyses))

class Convertor(object):
	def __init__(self, rule_file):
		self.conversion_rules = self._load_conversion_rules(rule_file)
		self.input_patterns = re.compile('(' + '|'.join(self.conversion_rules['sym']) + ')')

	def _convert_tags(self, t):
		"""
			Turn v|tv into <v><tv> and p1|sg into <p1><sg>
		"""
		if t != '':
			return '<' + t.replace('|', '><') + '>'
		return t

	def _load_conversion_rules(self, fn):
		rules = {'sym': set(), 'sub': []}
		for line in open(fn):
			if line[0] == '#':
				continue
			row = line.strip().split('\t')
			priority = int(row[0])
			score = priority
			inn = [re.sub('^_$', '', i) for i in row[1:5]]
			out = [re.sub('^_$', '', i) for i in row[5:]]
	
			if inn[0] != '': score += 4
			if inn[1] != '': score += 3
			if inn[2] != '': score += (2 * len(inn[2].split('|')))
			if inn[3] != '': score += 1
	
			inn = [inn[0], self._convert_tags(inn[1]), self._convert_tags(inn[2]), inn[3]] 
			rules['sym'].add(inn[1])
			rules['sym'].add(inn[2])
			rules['sub'].append((score, inn, out))
	
		rules['sym'] = list(rules['sym'])
		rules['sym'].sort(key=lambda x:len(x), reverse=True)
		rules['sub'].sort()
		return rules



	def _convert(self, a):
		"""
			Convert an analysis to UD using the conversion rules, rules
			are applied in priority order.
		"""
		analysis = {'lemma':'', 'pos':'', 'feats': set()}
		tags = [i for i in self.input_patterns.findall(a) if not i == '']
		msd = set(tags)
		analysis['lemma'] = re.sub('<[^>]+>', '', a)
		for (priority, inn, out) in self.conversion_rules['sub']:
			pos_pat = set([inn[1]])
			remainder = msd - pos_pat
			intersect = msd.intersection(pos_pat)
			if intersect == pos_pat:
				analysis['pos'] = out[1]
				if out[2] != '':
					for i in out[2].split('|'):
						analysis['feats'].add(i)
				msd = remainder
			feats_pat = set([inn[2]])
			remainder = msd - feats_pat
			intersect = msd.intersection(feats_pat)
			if intersect == feats_pat:
				for i in out[2].split('|'):
					analysis['feats'].add(i)
				msd = remainder

		return analysis

	def convert(self, analysis_):
		analysis = []	
		subwords = analysis_.split('+')
		for word in subwords:
			analysis.append(self._convert(word))
		return analysis

class Analyser(object):

	def __init__(self, tokeniser=None, normalise=False, log_level="error"):
		if not tokeniser:
			self.tokenise = self._tokenise
		else:
			self.tokenise = tokeniser

		with pkg_resources.path("elotl.nahuatl.data", "nhi.mor.att") as p:
			_path_to_att_dir = p
		with pkg_resources.path("elotl.nahuatl.data", "nhi.mor.tsv") as p:
			_path_to_tsv_dir = p

		self.analyser = ATTFST(_path_to_att_dir)
		self.convertor = Convertor(_path_to_tsv_dir)

	def _tokenise(self, text):
		tokens = re.sub('([^a-zA-Z]+)', ' \g<1> ', text)
		return [token.strip() for token in tokens.split(' ') if not token.strip() == '']

	def _convert_analysis(self, analysis):
		analyses = self.convertor.convert(analysis)
		return analyses

	def _analyse_token(self,token, alternative=''):
		analyses = list(self.analyser.apply(token))
		if len(analyses) == 0:
			analyses = list(self.analyser.apply(alternative))
				
		converted = []
		for (analysis, weight) in analyses:
			converted.append((self._convert_analysis(analysis), weight))
		return converted

	def analyse(self, text, tokenise = False):
		"""
			An analyse function that can take either a string with a tokeniser, 
			a pre-tokenised list or a pre-tokenised string. If it is passed a 
			tokeniser the tokeniser is first run and then the list is analysed,
			if passed a list, the list is analysed, if passed a pre-tokenised
			list then the list is split on space and then analysed.

			>>> a.analyse('a b c')
			[<Token "a" (0)>, <Token "b" (0)>, <Token "c" (0)>]
			>>> a.analyse(['a', 'b', 'c'])
			[<Token "a" (0)>, <Token "b" (0)>, <Token "c" (0)>]
			>>> a.analyse('ab, c', tokenise=True)
			[<Token "a" (0)>, <Token "b" (0)>, <Token "," (0)>, <Token "c" (0)>]
		"""

		tokens = []
		wordforms = []
		if tokenise == False:
			if type(text) == str:
				wordforms = text.split(' ')
			elif type(text) == list:
				wordforms = text
		else:
			wordforms = self.tokenise(text)	

		for wordform in wordforms:
			analyses = self._analyse_token(wordform, wordform.lower())
			token = Token(wordform, analyses)
			tokens.append(token)

		return tokens

