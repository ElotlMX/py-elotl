import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elotl",
    version="0.0.1.10",
    author="Paul Aguilar (@penserbjorne)",
    author_email="paul.aguilar.enriquez@hotmail.com",
    description="Paquete para PLN de lenguas originarias",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ElotlMX/py-elotl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Development Status :: 2 - Pre-Alpha",
    ],
    python_requires='>=3',
    install_requires=[
        'importlib_resources'
    ],
    include_package_data=True,
    zip_safe=True,
)
