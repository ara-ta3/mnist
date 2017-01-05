run: bin/python
	$< main.py

install: bin/pip requirements.txt
	$< install -r requirements.txt

install-dev: bin/pip requirements.dev.txt install
	$< install -r requirements.dev.txt

pyvenv:
	pyvenv .

bin/pip:
	$(MAKE) pyvenv

bin/python:
	$(MAKE) pyvenv

mnist/dataload.py:
	wget -O $@ https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch/master/dataset/mnist.py

