FST_DIR = $(CURDIR)/elotl/utils/fst
LEXC_DIR_NAHUATL = $(FST_DIR)/lexc/nahuatl
HFST_DIR_NAHUATL = $(FST_DIR)/hfst/nahuatl
ATT_DIR_NAHUATL = $(FST_DIR)/att/nahuatl

LEXC_DIR_OTOMI = $(FST_DIR)/lexc/otomi
HFST_DIR_OTOMI = $(FST_DIR)/hfst/otomi
ATT_DIR_OTOMI = $(FST_DIR)/att/otomi

all: fst build_python

fst:
	rm -rf $(HFST_DIR_NAHUATL) $(ATT_DIR_NAHUATL) $(HFST_DIR_OTOMI) $(ATT_DIR_OTOMI)
	mkdir -p $(HFST_DIR_NAHUATL) $(ATT_DIR_NAHUATL) $(HFST_DIR_OTOMI) $(ATT_DIR_OTOMI)
	touch $(ATT_DIR_NAHUATL)/__init__.py
	touch $(ATT_DIR_OTOMI)/__init__.py

	hfst-lexc $(LEXC_DIR_NAHUATL)/orig-fon.lexc -o $(HFST_DIR_NAHUATL)/orig-fon.hfst
	hfst-lexc $(LEXC_DIR_NAHUATL)/fon-sep.lexc -o $(HFST_DIR_NAHUATL)/fon-sep.hfst
	hfst-lexc $(LEXC_DIR_NAHUATL)/fon-inali.lexc -o $(HFST_DIR_NAHUATL)/fon-inali.hfst
	hfst-lexc $(LEXC_DIR_NAHUATL)/fon-ack.lexc -o $(HFST_DIR_NAHUATL)/fon-ack.hfst
	hfst-lexc $(LEXC_DIR_NAHUATL)/fon-ilv.lexc -o $(HFST_DIR_NAHUATL)/fon-ilv.hfst

	hfst-compose -1 $(HFST_DIR_NAHUATL)/orig-fon.hfst -2 $(HFST_DIR_NAHUATL)/fon-sep.hfst -o $(HFST_DIR_NAHUATL)/orig-sep.hfst
	hfst-compose -1 $(HFST_DIR_NAHUATL)/orig-fon.hfst -2 $(HFST_DIR_NAHUATL)/fon-inali.hfst -o $(HFST_DIR_NAHUATL)/orig-inali.hfst
	hfst-compose -1 $(HFST_DIR_NAHUATL)/orig-fon.hfst -2 $(HFST_DIR_NAHUATL)/fon-ack.hfst -o $(HFST_DIR_NAHUATL)/orig-ack.hfst
	hfst-compose -1 $(HFST_DIR_NAHUATL)/orig-fon.hfst -2 $(HFST_DIR_NAHUATL)/fon-ilv.hfst -o $(HFST_DIR_NAHUATL)/orig-ilv.hfst

	hfst-fst2txt $(HFST_DIR_NAHUATL)/orig-fon.hfst > $(ATT_DIR_NAHUATL)/orig-fon.att
	hfst-fst2txt $(HFST_DIR_NAHUATL)/fon-sep.hfst > $(ATT_DIR_NAHUATL)/fon-sep.att
	hfst-fst2txt $(HFST_DIR_NAHUATL)/fon-inali.hfst > $(ATT_DIR_NAHUATL)/fon-inali.att
	hfst-fst2txt $(HFST_DIR_NAHUATL)/fon-ack.hfst > $(ATT_DIR_NAHUATL)/fon-ack.att
	hfst-fst2txt $(HFST_DIR_NAHUATL)/fon-ilv.hfst > $(ATT_DIR_NAHUATL)/fon-ilv.att


	hfst-lexc $(LEXC_DIR_OTOMI)/orig-fon.lexc -o $(HFST_DIR_OTOMI)/orig-fon.hfst
	hfst-lexc $(LEXC_DIR_OTOMI)/fon-inali.lexc -o $(HFST_DIR_OTOMI)/fon-inali.hfst
	hfst-lexc $(LEXC_DIR_OTOMI)/fon-otq.lexc -o $(HFST_DIR_OTOMI)/fon-otq.hfst
	hfst-lexc $(LEXC_DIR_OTOMI)/fon-ots.lexc -o $(HFST_DIR_OTOMI)/fon-ots.hfst
	hfst-lexc $(LEXC_DIR_OTOMI)/fon-rfe.lexc -o $(HFST_DIR_OTOMI)/fon-rfe.hfst

	hfst-compose -1 $(HFST_DIR_OTOMI)/orig-fon.hfst -2 $(HFST_DIR_OTOMI)/fon-inali.hfst -o $(HFST_DIR_OTOMI)/orig-inali.hfst
	hfst-compose -1 $(HFST_DIR_OTOMI)/orig-fon.hfst -2 $(HFST_DIR_OTOMI)/fon-otq.hfst -o $(HFST_DIR_OTOMI)/orig-otq.hfst
	hfst-compose -1 $(HFST_DIR_OTOMI)/orig-fon.hfst -2 $(HFST_DIR_OTOMI)/fon-ots.hfst -o $(HFST_DIR_OTOMI)/orig-ots.hfst
	hfst-compose -1 $(HFST_DIR_OTOMI)/orig-fon.hfst -2 $(HFST_DIR_OTOMI)/fon-rfe.hfst -o $(HFST_DIR_OTOMI)/orig-rfe.hfst

	hfst-fst2txt $(HFST_DIR_OTOMI)/orig-fon.hfst > $(ATT_DIR_OTOMI)/orig-fon.att
	hfst-fst2txt $(HFST_DIR_OTOMI)/fon-inali.hfst > $(ATT_DIR_OTOMI)/fon-inali.att
	hfst-fst2txt $(HFST_DIR_OTOMI)/fon-otq.hfst > $(ATT_DIR_OTOMI)/fon-otq.att
	hfst-fst2txt $(HFST_DIR_OTOMI)/fon-ots.hfst > $(ATT_DIR_OTOMI)/fon-ots.att
	hfst-fst2txt $(HFST_DIR_OTOMI)/fon-rfe.hfst > $(ATT_DIR_OTOMI)/fon-rfe.att

build_python:
	rm -rf build/ dist/
	python -m pip install --upgrade pip
	poetry build
	python -m pip install -e .
