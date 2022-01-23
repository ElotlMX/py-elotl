# Morphology

## The transducer file

A morphological analyser is distributed as a finite-state transducer in the ATT 
format, this is a five column tab-separated format with an input and output
state, an input and output symbol and a weight.

```
0	1	m	@0@	0.000000
```

Here the input state is `0`, the output state is `1`, and the input symbol is `m` 
and the output symbol is `@0@`, which stands for epsilon. The weight is `0.000000`.

```
11721	11734	@0@	<pr>	0.000000
```

Here the output symbol is a tag, `<pr>` for preposition.

## Tags

The internal representation of morphological tags in the analyser is an mnemonic 
encased in less-than and greater-than symbols, for example `<o_sg3>` stands
for object agreement, third person singular.

## The tagset conversion file

In addition to the `.att` file which contains the transducer, each analyser has 
a `.tsv` file which manages tagset conversion, from individual tags, e.g. `<o_sg3>`
to Feature=Value pairs, e.g.

```python
{'Number[obj]': 'Sing', 'Person[obj]': '3'}
```

The conversion file consists of nine columns, a priority column and then four columns
of input and four columns of output. 

The four columns are:
- Lemma
- POS
- Tags / features
- Dependency relation

Currently the dependency relation is not used.

An example rule would be:

```
1	_	_	o_aa3	_	_	_	Person[obj]=3|Animacy[obj]=Anim	_
```

Which would convert the tag `<o_aa3>` into the set `{'Animacy[obj]': 'Anim', 'Person[obj]': '3'}`

Another example would be:

```
2	_	prn	pers	_	_	PRON	PronType=Prs	_
```

Which would convert the tags `<prn><pers>` into the part-of-speech tag `PRON` with the features 
`{'PronType':'Prs'}`.
