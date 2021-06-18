all:
	hfst-lexc lexc/orig-fon.lexc -o hfst/orig-fon.hfst
	hfst-lexc lexc/fon-sep-u-j.lexc -o hfst/fon-sep-u-j.hfst
	hfst-lexc lexc/fon-sep-w-h.lexc -o hfst/fon-sep-w-h.hfst
	hfst-lexc lexc/fon-ack.lexc -o hfst/fon-ack.hfst
	hfst-compose -1 hfst/orig-fon.hfst -2 hfst/fon-sep-u-j.hfst -o hfst/orig-sep-u-j.hfst
	hfst-compose -1 hfst/orig-fon.hfst -2 hfst/fon-sep-w-h.hfst -o hfst/orig-sep-w-h.hfst
	hfst-compose -1 hfst/orig-fon.hfst -2 hfst/fon-ack.hfst -o hfst/orig-ack.hfst

clean:
	rm hfst/*.hfst