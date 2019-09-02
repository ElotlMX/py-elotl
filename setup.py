import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elotl-pln",
    version="0.0.1",
    author="ElotlMX<->Penserbjorne",
    author_email="paul.aguilar.enriquez@hotmail.com",
    description="Paquete para PLN de lenguas originarias",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ElotlMX/elotl_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
