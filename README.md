# Py-Elotl

Python package for Natural Language Processing (NLP), focused on low-resource languages spoken in Mexico.

This is a project of [Comunidad Elotl](https://elotl.mx/).

Developed by:
- Paul Aguilar [@penserbjorne](https://github.com/penserbjorne), [paul.aguilar.enriquez@hotmail.com](mailto:paul.aguilar.enriquez@hotmail.com)
- Robert Pugh [@Lguyogiro](https://github.com/Lguyogiro), [robertpugh408@gmail.com](mailto:robertpugh408@gmail.com)

Requiere python>=3.X

- Development Status `Pre-Alpha`. Read [Classifiers](https://pypi.org/classifiers/)
- pip package: [elotl](https://pypi.org/project/elotl/)
- GitHub repository: [ElotlMX/py-elotl](https://github.com/ElotlMX/py-elotl)

## Installation

### Using `pip`

```bash
pip install elotl
```

### From source

```bash
git clone https://github.com/ElotlMX/py-elotl.git
cd py-elotl
pip install -e .
```

## Use

### Working with corpus

```python
import elotl.corpus
```

#### Listing available corpus

Code:

```python
print("Name\t\tDescription")
list_of_corpus = elotl.corpus.list_of_corpus()
for row in list_of_corpus:
    print(row)
```

Output:

```bash
Name		Description
['axolotl', 'Is a Spanish-Nahuatl parallel corpus']
['tsunkua', 'Is a Spanish-otomí parallel corpus']

```

#### Loading a corpus

If a non-existent corpus is requested, a value of 0 is returned.

```python
axolotl = elotl.corpus.load('axolotlr')
if axolotl == 0:
    print("The name entered does not correspond to any corpus")
```

If an existing corpus is entered, a list is returned.

```python
axolotl = elotl.corpus.load('axolotl')
for row in axolotl:
    print(row)
```

```bash
['Hay que adivinar: un pozo, a la mitad del cerro, te vas a encontrar.', 'See tosaasaanil, see tosaasaanil. Tias iipan see tepeetl, iitlakotian tepeetl, tikoonextis san see aameyalli.', '', 'Adivinanzas nahuas']
```

Each element of the list has four indices:

- non_original_language
- original_language
- variant
- document_name

```python
tsunkua = elotl.corpus.load('tsunkua')
  for row in tsunkua:
      print(row[0]) # language 1
      print(row[1]) # language 2
      print(row[2]) # variant
      print(row[3]) # document
```

```bash
Una vez una señora se emborrachó
nándi na ra t'u̱xú bintí
Otomí del Estado de México (ots)
El otomí de toluca, Yolanda Lastra

```

### Normalizing nahuatl orthographies

Import the orthography module and Load the axolot nahuatl corpus.

```python
import elotl.corpus
import elotl.nahuatl.orthography
a = elotl.corpus.load("axolotl")
```

Creates a normalizer object, passing as parameter the normalization to be used.

The following normalizations are currently available:

- sep
  - Alphabet often seen in use by the Secretaría de Educación Pública (SEP) and the Instituto Nacional para la Educación de los Adultos (INEA). important characteristics of this alphabet are the use of "u" for the phoneme /w/, "k" for /k/, and "j" for /h/.
- inali
  - Alphabet in use by the Instituto Nacional de Lenguas Indígenas. Uses "w" for /w/, "k" for /k/, and "h" for /h/.
- ack
  - Alphabet initially used by Richard Andrews and subsequently by a number of other Nahuatl scholars. Named after Andrews, Campbell, and Karttunen. Uses "hu" for /w/, "c" and "qu" for /k/, and "h" for /h/.

If an unsupported normalization is specified, sep will be used by default.

You can use the `normalize` method to normalize a text to the selected orthography. And the `to_phones` method to get
the phonemes.

```python
>>> n = elotl.nahuatl.orthography.Normalizer("sep")
>>> n.normalize(a[1][1])
'au in ye yujki in on tlenamakak niman ye ik teixpan on motlalia se tlakatl itech mokaua.'
>>> n.to_phones(a[1][1])
'aw in ye yuʔki in on ƛenamakak niman ye ik teiʃpan on moƛalia se ƛakaƛ itet͡ʃ mokawa.'
```

```python
>>> n = elotl.nahuatl.orthography.Normalizer("inali")
>>> n.normalize(a[1][1])
'aw in ye yuhki in on tlenamakak niman ye ik teixpan on motlalia se tlakatl itech mokawa.'
>>> n.to_phones(a[1][1])
'aw in ye yuʔki in on ƛenamakak niman ye ik teiʃpan on moƛalia se ƛakaƛ itet͡ʃ mokawa.'
```

```python
>>> n = elotl.nahuatl.orthography.Normalizer("ack")
>>> n.normalize(a[1][1])
'auh in ye yuhqui in on tlenamacac niman ye ic teixpan on motlalia ce tlacatl itech mocahua.'
>>> n.to_phones(a[1][1])
'aw in ye yuʔki in on ƛenamakak niman ye ik teiʃpan on moƛalia se ƛakaƛ itet͡ʃ mokawa.'
```
## Package structure

The following structure is a reference. As the package grows it will be better documented.

```
elotl/                              Top-level package
          __init__.py               Initialize the package
          corpora/                  Here are the corpus data
          corpus/                   Subpackage to load corpus     
          nahuatl/                  Nahuatl language subpackage
                  orthography.py    Module to normalyze nahuatl orthography and phonemas
          utils/                    Subpackage with useful functions and files
                  fst/              Finite State Transducer functions
                        att/        Module with static .att files
test/                               Unit test scripts
```

## Development

### Requirements

- python3
- [HFST](https://github.com/hfst/hfst)
- GNU make
- virtualenv
- Python packages
  - setuptools
  - wheel

### Quick build

```bash
virtualenv --python=/usr/bin/python3 venv
source venv/bin/activate
make all
```

### Step by step

#### Build FSTs

Build the FSTs with `make`.

```bash
make fst
```

#### Create a virtual environment and activate it.

```bash
virtualenv --python=/usr/bin/python3 venv
source venv/bin/activate
```

#### Update `pip` and generate distribution files.

```bash
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools wheel
rm -rf build/ dist/
python setup.py clean sdist bdist_wheel
```

### Testing the package locally

```bash
python -m pip install -e .
```

### Send to PyPI

```bash
python -m pip install twine
twine upload dist/*
```

## License

[Mozilla Public License 2.0 (MPL 2.0)](./LICENSE)

## References

- [https://elotl.mx/](https://elotl.mx/)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [How To Package Your Python Code](https://python-packaging.readthedocs.io/en/latest/minimal.html)
- [Making a Python Package](https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html)
