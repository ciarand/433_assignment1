tests:
	./bin/py.test

clean:
	rm -rf *.pyc pip-selfcheck.json __pycache__

.PHONY: tests clean
