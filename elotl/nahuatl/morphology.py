# -*- coding: UTF-8 -*-

# Ejemplo de uso:

#	>>> from elotl.nahuatl.morphology import Analyser
#	>>> a = Analyser()
#	>>> res = a.analyse('Huan nomama onechilhuaya, “Amo quen ximati, teh xiyo in escuela.', tokenise=True)

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

	Parameters
	----------

	"""
	def __init__(self, wordform, analyses = []):
		self.wordform = wordform
		self.analyses = analyses

	def __repr__(self):
		return '<Token "{0}" ({1})>'.format(self.wordform,len(self.analyses))

class Convertor(object):
	"""
	A class to convert from Apertium-style analyses to UD-compatible analyses by
	means of a sequence of priority-ordered rules.

	Parameters
	----------
	rule_file: str
		A path to the location of the TSV file containing the tagset conversion rules.
		Each rule is composed of 9 columns: 
			1. Priority
			2. Input lemma
			3. Input POS
			4. Input features
			5. Input dependency relation (unused)
			6. Output lemma
			7. Output POS
			8. Output features
			9. Output dependency relation (unused)

	"""
	def __init__(self, rule_file):
		self.conversion_rules = self._load_conversion_rules(rule_file)
		self.input_patterns = re.compile('(' + '|'.join(self.conversion_rules['sym']) + ')')

	def _convert_tags(self, tags):
		"""
		Convert from the tag format in the TSV rule-file to tags that will match
		the Apertium analyses, e.g. v|tv → <v><tv> and p1|sg → <p1><sg>

		Parameters
		----------
		tags: str
			A sequence of tags separated by the pipe symbol, |

		Returns 
		----------
		str
			A sequences of tags encased in less-than and greater-than < > 
		"""

		if tags != '':
			return '<' + tags.replace('|', '><') + '>'
		return tags

	def _load_conversion_rules(self, fn):
		"""
		Loads the conversion rules and scores each rule. Longer rules are scored higher,
		rules containing lemmas are scored higher.

		Parameters
		----------
		fn: str
			A path to the location of the TSV file containing the tagset conversion rules.

		Returns 
		----------
		dict
			A dictionary containing a set of symbols used for matching and a list of
			substitution rules.
		"""

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

		Parameters
		----------
		a: str
			An Apertium-compatible analysis, e.g. <s_sg1>quiza<v><iv><pret>, note
			that by this point there should be no subwords.

		Returns 
		----------
		dict
			A dictionary containing a lemma, a part-of-speech and a 
			set of Feature=Value pairs.
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
		"""
		The main function for conversion, takes a full analysis, including possible
		subwords, e.g. ya<adv>+<s_sg1>quiza<v><iv><pret> and returns a list of 
		syntactic words. 

		Parameters
		----------
		analysis_: str
			An Apertium-compatible analysis.

		Returns 
		----------
		list
			A list of the component analyses by syntactic word.
		"""

		analysis = []	
		subwords = analysis_.split('+')
		for word in subwords:
			analysis.append(self._convert(word))
		return analysis

class Analyser(object):
	"""
	Class for returning morphological analyses in a Python-friendly format with UD style
	POS tags and Feature=Value pairs.

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

		with pkg_resources.path("elotl.nahuatl.data", "nhi.mor.att") as p:
			_path_to_att_dir = p
		with pkg_resources.path("elotl.nahuatl.data", "nhi.mor.tsv") as p:
			_path_to_tsv_dir = p

		self.analyser = ATTFST(_path_to_att_dir)
		self.convertor = Convertor(_path_to_tsv_dir)

	def _tokenise(self, text):
		"""
		Internal backoff tokenisation function. 

		Parameters
		----------
		text: str
			The text to be tokenised.

		Returns 
		----------
		list
			List of space separated tokens.
		
		"""

		tokens = re.sub('([^a-zA-Z]+)', ' \g<1> ', text)
		return [token.strip() for token in tokens.split(' ') if not token.strip() == '']

	def _convert_analysis(self, analysis):
		"""
		Takes an analysis returned by the transducer and converts it to a more Python-friendly
		format. 

		Parameters
		----------
		analysis: str
			An analysis for a surface token, e.g. ya<adv>+<s_sg1>quiza<v><iv><pret>

		Returns 
		----------
		list
			A list of syntactic words with their analyses in UD format
			[{'lemma': 'ya', 'pos': 'ADV', 'feats': set()}, 
				{'lemma': 'quiza', 'pos': 'VERB', 'feats': {
				'Number[subj]=Sing', 'Person[subj]=1', 'Tense=Past', 'VerbForm=Fin', 'Subcat=Intr'}}]
		"""

		analyses = self.convertor.convert(analysis)
		return analyses

	def _analyse_token(self,token, alternative=''):
		"""
		Function that takes a token and returns a list of analyses with their 
		weights as assigned by the transducer.

		Parameters
		----------
		token: str
			A surface token

		alternative: str
			An alternative form, e.g. a lowercased or normalised form

		Returns 
		----------
		list
			A list of the possible analyses with weights
		"""
		analyses = list(self.analyser.apply(token))
		if len(analyses) == 0 and alternative:
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


		Parameters
		----------
		text: str or list
			Input text/sentence. It can be either a string or a list. It
			should be pre-tokenised, alternatively see below.
		
		tokenise: bool
			Should tokenisation be performed on the input prior to analysis?
			
		Returns
		----------
		list
			List of Token objects.

		Examples
		----------

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

	def analyze(self, text, tokenize = False):
		"""
		Convenience alias of analyse() with alternative spelling.

		Parameters
		----------
		text: str or list
			Input text/sentence. It can be either a string or a list. It
			should be pre-tokenised, alternatively see below.
		
		tokenize: bool
			Should tokenisation be performed on the input prior to analysis?
			
		Returns
		----------
		list
			List of Token objects.
		"""
		return self.analyse(text, tokenize)

# Convenience alias for Analyser to Analyzer
Analyzer = Analyser
