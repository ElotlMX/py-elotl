# Elotl Package

Paquete de Python3 con algoritmos e implementaciones de la comunidad Elotl para
PLN de lenguas originaria.

- Paquete en estado de `Planeación`. Revisar [Classifiers](https://pypi.org/classifiers/)
- Repositorio de desarrollo: [ElotlMX/elotl_pkg](https://github.com/ElotlMX/elotl_pkg)
- Paquete en pip: [elotl](https://pypi.org/project/elotl/)

## Instalación

### Desde la fuente

```bash
git clone https://github.com/ElotlMX/elotl_pkg.git
cd elotl_pkg
pip install -e .
```

### Utilizando `pip`

```bash
pip install elotl
```

## Uso

### Importar por separado

```python3
>>> import elotl
>>> import elotl.nahuatl
>>> import elotl.otomi
>>> import elotl.wixarika
>>> elotl.test()
'Test paquete elotl satisfactorio'
>>> elotl.nahuatl.test()
'Test subpaquete elotl-nahuatl satisfactorio'
>>> elotl.otomi.test()
'Test subpaquete elotl-otomi satisfactorio'
>>> elotl.wixarika.test()
'Test subpaquete elotl-wixarika satisfactorio'
```

### Importar todo

```python3
>>> from elotl import *
>>> nahuatl.test()
'Test subpaquete elotl-nahuatl satisfactorio'
>>> otomi.test()
'Test subpaquete elotl-otomi satisfactorio'
>>> wixarika.test()
'Test subpaquete elotl-wixarika satisfactorio'
```

## Estructura del paquete

La siguiente estructura es una referencia. Conforme el paquete crezca se ira
documentando mejor.

```bash
elotl/                              Top-level package
          __init__.py               Inicializar el paquete
          nahuatl/                  Subpaquete para el idioma nahuatl
                  __init__.py
                  corpus.py
                  stemmer.py
                  ...
          otomi/                    Subpaquete para el idioma otomi
                  __init__.py
                  corpus.py
                  stemmer.py
                  ...
          wixarika/                 Subpaquete para el idioma wixarika
                  __init__.py
                  corpus.py
                  stemmer.py
                  ...
```

## Desarrollo

### Crear un entorno virtual y activarlo.

```bash
virtualenv --python=/usr/bin/python3 elotl-venv
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
pip install -e .
```

### Enviar a PyPI

```bash
pip install twine
twine upload dist/*
```

## Licencia

[Mozilla Public License 2.0 (MPL 2.0)](./LICENSE)

## Referencias

- [https://elotl.mx/](https://elotl.mx/)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [How To Package Your Python Code](https://python-packaging.readthedocs.io/en/latest/minimal.html)
