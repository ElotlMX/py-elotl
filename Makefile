FST_DIR = $(CURDIR)/elotl/utils/fst
LEXC_DIR = $(FST_DIR)/lexc
HFST_DIR = $(FST_DIR)/hfst
ATT_DIR = $(FST_DIR)/att

all: clean_fst fst

fst:
	mkdir -p $(HFST_DIR) $(ATT_DIR)
	hfst-lexc $(LEXC_DIR)/orig-fon.lexc -o $(HFST_DIR)/orig-fon.hfst
	hfst-lexc $(LEXC_DIR)/fon-sep-u-j.lexc -o $(HFST_DIR)/fon-sep-u-j.hfst
	hfst-lexc $(LEXC_DIR)/fon-sep-w-h.lexc -o $(HFST_DIR)/fon-sep-w-h.hfst
	hfst-lexc $(LEXC_DIR)/fon-ack.lexc -o $(HFST_DIR)/fon-ack.hfst

	hfst-compose -1 $(HFST_DIR)/orig-fon.hfst -2 $(HFST_DIR)/fon-sep-u-j.hfst -o $(HFST_DIR)/orig-sep-u-j.hfst
	hfst-compose -1 $(HFST_DIR)/orig-fon.hfst -2 $(HFST_DIR)/fon-sep-w-h.hfst -o $(HFST_DIR)/orig-sep-w-h.hfst
	hfst-compose -1 $(HFST_DIR)/orig-fon.hfst -2 $(HFST_DIR)/fon-ack.hfst -o $(HFST_DIR)/orig-ack.hfst

	hfst-fst2txt $(HFST_DIR)/orig-fon.hfst > $(ATT_DIR)/orig-fon.att
	hfst-fst2txt $(HFST_DIR)/fon-sep-u-j.hfst > $(ATT_DIR)/fon-sep-u-j.att
	hfst-fst2txt $(HFST_DIR)/fon-sep-w-h.hfst > $(ATT_DIR)/fon-sep-w-h.att
	hfst-fst2txt $(HFST_DIR)/fon-ack.hfst > $(ATT_DIR)/fon-ack.att

clean_fst:
	rm -rf $(HFST_DIR) $(ATT_DIR)
