all:
	hfst-lexc lexc/orig-fon.lexc -o hfst/orig-fon.hfst
	hfst-lexc lexc/fon-sep.lexc -o hfst/fon-sep.hfst
	hfst-lexc lexc/fon-ack.lexc -o hfst/fon-ack.hfst
	hfst-compose -1 hfst/orig-fon.hfst -2 hfst/fon-sep.hfst -o hfst/orig-sep.hfst
	hfst-compose -1 hfst/orig-fon.hfst -2 hfst/fon-ack.hfst -o hfst/orig-ack.hfst

clean:
	rm hfst/*.hfst