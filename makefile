MAKEFLAGS += -s

install:
	echo installing command..
	chmod +x src/wrapper.py
	sudo cp src/wrapper.py /usr/local/bin/aigen
	echo copying tools to destination..
	chmod +x src/aigen.py
	rm -rf ~/.aigen
	mkdir ~/.aigen
	find src ! -name 'wrapper.py' -exec cp {} ~/.aigen \;
	echo DONE!
