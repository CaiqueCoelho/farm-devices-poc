include .env
export


setup:
	source venv/bin/activate
	pip3 install -r requirements.txt

run-bsk:
	python3 browserstack-poc.py