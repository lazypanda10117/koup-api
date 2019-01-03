## ----- Variables -----
ENV = 1 # 0 for production, 1 for development
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
.PHONY: dev-run install prod-init prod-update prod-run

## FLSK starts the flask server.
FLSK = pipenv run flask run

dev-run:
	@echo "Starting Flask server ($(ENV))..."
	@if [ "$(ENV)" -eq 1 ]; then \
	   export FLASK_ENV=development && export FLASK_DEBUG=1 && \
	          $(FLSK); \
	 else \
	   export FLASK_ENV=production && $(FLSK); \
	 fi

install:
	@echo "Installing dependencies using 'pipenv'..."
	@pipenv install --dev

prod-init:
	@flask db init
	@flask db migrate
	@flask db upgrade
	@gunicorn app:app

prod-update:
	@flask db migrate
	@flask db upgrade
	@gunicorn app:app

prod-run:
	@gunicorn app:app --preload
