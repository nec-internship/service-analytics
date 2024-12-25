PY3=python3
PIP3=pip3

VENV=venv
BIN=$(VENV)/bin

venv: 
	$(PY3) -m venv venv

up:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down 

build: 
	sudo docker build . -t nec-internship/service-analytics:latest -f Dockerfile

all:
	@make down
	@make build
	@make up 

restart:
	@make down 
	@make up

install: 
	poetry install

run-dev: 
	$(PY3) -m run.dev

logs:
	docker logs nec-sa -f 

lint:
	pylint ./src

clean-$(VENV):
	rm -rf $(VENV)

clean-cache:
	sudo find . -type f -name *.pyc -delete
	sudo find . -type d -name __pycache__ -delete

.PHONY: venv lint clean-$(VENV) clean-cache run-dev install up down