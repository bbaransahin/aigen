MAKEFLAGS += -s

install:
	echo making codes executable..
	chmod +x src/wrapper.py
	chmod +x src/aigen.py
	echo installing command..
	sudo cp src/wrapper.py /usr/local/bin/aigen
	echo removing and creating again the aigen dir..
	rm -rf ~/.aigen
	mkdir ~/.aigen
	echo copying tools to destination..
	find src ! -name 'wrapper.py' -exec cp {} ~/.aigen \;
	echo generating convos directory..
	mkdir ~/.aigen/convos
	echo DONE!
