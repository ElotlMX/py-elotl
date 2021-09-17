FST_DIR = $(CURDIR)/elotl/utils/fst
LEXC_DIR = $(FST_DIR)/lexc
HFST_DIR = $(FST_DIR)/hfst
ATT_DIR = $(FST_DIR)/att

all: fst build_python

fst:
	rm -rf $(HFST_DIR) $(ATT_DIR)
	mkdir -p $(HFST_DIR) $(ATT_DIR)
	touch $(ATT_DIR)/__init__.py

	hfst-lexc $(LEXC_DIR)/orig-fon.lexc -o $(HFST_DIR)/orig-fon.hfst
	hfst-lexc $(LEXC_DIR)/fon-sep.lexc -o $(HFST_DIR)/fon-sep.hfst
	hfst-lexc $(LEXC_DIR)/fon-inali.lexc -o $(HFST_DIR)/fon-inali.hfst
	hfst-lexc $(LEXC_DIR)/fon-ack.lexc -o $(HFST_DIR)/fon-ack.hfst

	hfst-compose -1 $(HFST_DIR)/orig-fon.hfst -2 $(HFST_DIR)/fon-sep.hfst -o $(HFST_DIR)/orig-sep.hfst
	hfst-compose -1 $(HFST_DIR)/orig-fon.hfst -2 $(HFST_DIR)/fon-inali.hfst -o $(HFST_DIR)/orig-inali.hfst
	hfst-compose -1 $(HFST_DIR)/orig-fon.hfst -2 $(HFST_DIR)/fon-ack.hfst -o $(HFST_DIR)/orig-ack.hfst

	hfst-fst2txt $(HFST_DIR)/orig-fon.hfst > $(ATT_DIR)/orig-fon.att
	hfst-fst2txt $(HFST_DIR)/fon-sep.hfst > $(ATT_DIR)/fon-sep.att
	hfst-fst2txt $(HFST_DIR)/fon-inali.hfst > $(ATT_DIR)/fon-inali.att
	hfst-fst2txt $(HFST_DIR)/fon-ack.hfst > $(ATT_DIR)/fon-ack.att

build_python:
	rm -rf build/ dist/
	python -m pip install --upgrade pip
	python -m pip install --upgrade setuptools wheel
	rm -rf build/ dist/
	python setup.py clean sdist bdist_wheel
	python -m pip install -e .