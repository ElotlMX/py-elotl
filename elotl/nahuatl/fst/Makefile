all:
	hfst-lexc lexc/orig-fon.lexc -o hfst/orig-fon.hfst
	hfst-lexc lexc/fon-sep.lexc -o hfst/fon-sep.hfst
	hfst-lexc lexc/fon-ack.lexc -o hfst/fon-ack.hfst

	hfst-compose -1 hfst/orig-fon.hfst -2 hfst/fon-sep.hfst -o hfst/orig-sep.hfst
	hfst-compose -1 hfst/orig-fon.hfst -2 hfst/fon-ack.hfst -o hfst/orig-ack.hfst

	hfst-fst2txt hfst/orig-fon.hfst > att/orig-fon.att
	hfst-fst2txt hfst/fon-sep.hfst > att/fon-sep.att
	hfst-fst2txt hfst/fon-ack.hfst > att/fon-ack.att

clean:
	rm hfst/*.hfst
	rm att/*.att
