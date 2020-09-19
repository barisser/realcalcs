

compile:
	pip-compile reqs.txt -o requirements.txt

install: compile
	. venv/bin/activate && pip install -r reqs.txt