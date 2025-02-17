# Py-Elotl

Python package for Natural Language Processing (NLP), focused on low-resource
languages spoken in Mexico.

This is a project of [Comunidad Elotl](https://elotl.mx/).

Developed by:
- Paul Aguilar [@penserbjorne](https://github.com/penserbjorne), [paul.aguilar.enriquez@hotmail.com](mailto:paul.aguilar.enriquez@hotmail.com)
- Robert Pugh [@Lguyogiro](https://github.com/Lguyogiro), [robertpugh408@gmail.com](mailto:robertpugh408@gmail.com)
- Diego Barriga [@umoqnier](https://github.com/umoqnier/), [dbarriga@ciencias.unam.mx](mailto:dbarriga@ciencias.unam.mx)

Requiere python>=3.8

- Development Status `Beta`. Read [Classifiers](https://pypi.org/classifiers/)
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

```python
[
    'Hay que adivinar: un pozo, a la mitad del cerro, te vas a encontrar.',
    'See tosaasaanil, see tosaasaanil. Tias iipan see tepeetl, iitlakotian tepeetl, tikoonextis san see aameyalli.',
    '',
    'Adivinanzas nahuas'
]
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

```
Una vez una señora se emborrachó
nándi na ra t'u̱xú bintí
Otomí del Estado de México (ots)
El otomí de toluca, Yolanda Lastra
```


## Package structure

The following structure is a reference. As the package grows it will be better
documented.

```
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── dist
├── docs
├── elotl                           Top-level package
    ├── corpora                     Here are the corpus data
    ├── corpus                      Subpackage to load corpus
    ├── huave                       Huave language subpackage
        └── orthography.py          Module to normalyze huave orthography and phonemas
    ├── __init__.py                 Initialize the package
    ├── nahuatl                     Nahuatl language subpackage
        └── orthography.py          Module to normalyze nahuatl orthography and phonemas
    ├── otomi                       Otomi language subpackage
        └── orthography.py          Module to normalyze otomi orthography and phonemas
    ├── __pycache__
    └── utils                       Subpackage with common functions and files
        └── fst                     Finite State Transducer functions
            └── att                 Module with static .att files
├── LICENSE
├── Makefile
├── MANIFEST.in
├── pyproject.toml
├── README.md
└── tests
```

## Development

### Requirements

- python>=3.8
- [HFST](https://github.com/hfst/hfst)
- GNU make
- [poetry](https://python-poetry.org/docs/)
    - For python packaging backend and virtualenvs

### Quick build

```bash
poetry env use 3.x
poetry shell
make all
```

Where `3.x` is your local python version. Check [managing environments with poetry](https://python-poetry.org/docs/managing-environments/)

### Step by step

#### Build FSTs

Build the FSTs with `make`.

```bash
make fst
```

#### Create a virtual environment and activate it.

```bash
poetry env use 3.x
poetry shell
```

#### Update `pip` and generate distribution files.

```bash
python -m pip install --upgrade pip
poetry build
```

### Testing the package locally

```bash
python -m pip install -e .
```

### Send to PyPI

```bash
poetry publish
```

Remember to [configure your PyPi credentials](https://python-poetry.org/docs/repositories/#configuring-credentials)

## License

[Mozilla Public License 2.0 (MPL 2.0)](./LICENSE)

## References

- [https://elotl.mx/](https://elotl.mx/)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [Libraries with poetry](https://python-poetry.org/docs/libraries/)
