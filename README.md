# Elotl Package

Paquete de Python con algoritmos e implementaciones de la comunidad Elotl para
PLN de lenguas originarias.

Requiere python>=3.7 .

- Paquete en estado de `Pre-Alpha`. Revisar [Classifiers](https://pypi.org/classifiers/)
- Paquete en pip: [elotl](https://pypi.org/project/elotl/)
- Repositorio de desarrollo: [ElotlMX/py-elotl](https://github.com/ElotlMX/py-elotl)

## Instalación

### Utilizando `pip`

```bash
pip install elotl
```

### Desde la fuente

```bash
git clone https://github.com/ElotlMX/py-elotl.git
cd py-elotl
pip install -e .
```

## Uso

<!--
### Importar por separado

```python
>>> import elotl
>>> import elotl.nahuatl
>>> import elotl.otomi
>>> elotl.test()
'Test paquete elotl satisfactorio'
>>> elotl.nahuatl.test()
'Test subpaquete elotl-nahuatl satisfactorio'
>>> elotl.otomi.test()
'Test subpaquete elotl-otomi satisfactorio'
```

### Importar todo

```python
>>> from elotl import *
>>> nahuatl.test()
'Test subpaquete elotl-nahuatl satisfactorio'
>>> otomi.test()
'Test subpaquete elotl-otomi satisfactorio'
```
-->

### Trabajando con corpus

```python
import elotl.corpus
```

#### Listando corpus disponibles

```python
print("Name\t\tDescription")
list_of_corpus = elotl.corpus.list_of_corpus()
for row in list_of_corpus:
    print(row)
```

La salida es la siguiente:

```bash
Name		Description
['axolotl', 'Is a nahuatl corpus']
['tsunkua', 'Is an otomí corpus']

```

#### Cargando un corpus

```python
# Si se solicita un corpus inexistente se retorna un valor 0
axolotl = elotl.corpus.load('axolotlr')
if axolotl == 0:
    print("El nombre ingresado no corresponde a ningun corpus")
```

```python
# Si se ingresa un corpus existente se retorna una lista
axolotl = elotl.corpus.load('axolotl')
for row in axolotl:
    print(row)
```

```bash
['Hay que adivinar: un pozo, a la mitad del cerro, te vas a encontrar.', 'See tosaasaanil, see tosaasaanil. Tias iipan see tepeetl, iitlakotian tepeetl, tikoonextis san see aameyalli.', '', 'Adivinanzas nahuas']
```

```python
# Cada elemento de la lista cuenta con cuatro indices:
# lengua_no_originaria, lengua_originaria, variante, nombre_de_documento
tsunkua = elotl.corpus.load('tsunkua')
  for row in tsunkua:
      print(row[0]) # lengua_no_originaria
      print(row[1]) # lengua_originaria
      print(row[2]) # variante
      print(row[3]) #nombre_de_documento
```

```bash
Una vez una señora se emborrachó
nándi na ra t'u̱xú bintí
Otomí del Estado de México (ots)
El otomí de toluca, Yolanda Lastra

```

## Estructura del paquete

La siguiente estructura es una referencia. Conforme el paquete crezca se ira
documentando mejor.

```bash
elotl/                              Top-level package
          __init__.py               Inicializar el paquete
          corpora/                  Aquí se encuentran los datos de los corpus
          corpus/                   Subpaquete para cargar corpus
                  __init__.py
                  corpus.py          
          nahuatl/                  Subpaquete para el idioma nahuatl
                  __init__.py
                  ...
          otomi/                    Subpaquete para el idioma otomi
                  __init__.py
                  ...
```

## Desarrollo

### Crear un entorno virtual y activarlo.

```bash
virtualenv --python=/usr/bin/python3.7 elotl-venv
source elotl-venv/bin/activate
```
### Actualizar `pip` y generar archivos de distribución.

```bash
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools wheel
python setup.py clean sdist bdist_wheel
```

### Probar el paquete local

```bash
python -m pip install -e .
```

### Enviar a PyPI

```bash
python -m pip install twine
twine upload dist/*
```

## Licencia

[Mozilla Public License 2.0 (MPL 2.0)](./LICENSE)

## Referencias

- [https://elotl.mx/](https://elotl.mx/)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [How To Package Your Python Code](https://python-packaging.readthedocs.io/en/latest/minimal.html)
