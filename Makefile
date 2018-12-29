## ----- Variables -----
ENV = dev
DB_VOL_NAME = postgres.data
STACK_NAME = $(shell basename $$PWD)

## Use git-secret.
SECRETS = true


## ----- Commands (targets) -----
.PHONY: default setup

## Default target when no arguments are given to make (run the program).
default: run

## Sets up this project on a new device.
setup: setup-hooks install
	@if [ "$(SECRETS)" == true ]; then $(REVEAL_SECRETS_CMD); fi


## [Git setup / configuration commands]
.PHONY: setup-hooks hide-secrets reveal-secrets

## Configure Git to use .githooks (for shared githooks).
setup-hooks:
	@echo "Configuring githooks..."
	@git config core.hooksPath .githooks && echo "done"

## Initialize git-secret
init-secrets:
	@git secret init

## Hide modified secret files using git-secret.
hide-secrets:
	@echo "Hiding modified secret files..."
	@git secret hide -m

## Reveal files hidden by git-secret.
REVEAL_SECRETS_CMD = git secret reveal
reveal-secrets:
	@echo "Revealing secret files..."
	@$(REVEAL_SECRETS_CMD)


## [Python commands]
.PHONY: prod run install clean

## FLSK starts the flask server.
FLSK = pipenv run flask run

run:
	@echo "Starting Flask server ($(ENV))..."
	@if [ "$(ENV)" == dev ]; then \
	   export FLASK_ENV=development && export FLASK_DEBUG=1 && \
	          $(FLSK); \
	 else \
	   export FLASK_ENV=production && $(FLSK); \
	 fi

install:
	@echo "Installing dependencies using 'pipenv'..."
	@pipenv install --dev


## [Docker commands]
.PHONY: up up-build-logs down prune prune-f

## DKCMP starts docker-compose using the dev config if ENV is dev.
DKCMP = docker-compose
DK = docker

## TARG is name of a particular target image / service.
TARG =
build:
	@$(DKCMP) build $(TARG)
up:
	@$(DKCMP) up -d $(TARG)
up-build-logs:
	@$(DKCMP) up-build logs $(TARG)
down:
	@$(DKCMP) down $(TARG)

## Prunes all Docker images, networks, and containers, in that order.
prune:
	@$(DK) container prune; $(DK) image prune; $(DK) network prune;
prune-f:
	@$(DK) container prune -f; $(DK) image prune -f; $(DK) network prune -f

## Removes the database data volume.
clean:
	@echo "Cleaning database data volume..."
	@$(DK) volume rm $(STACK_NAME)_$(DB_VOL_NAME)
