

install: bin/pip requirements.txt
	$< install -r requirements.txt

virtualenv:
	virtualenv -p python3 .

bin/pip:
	$(MAKE) virtualenv
