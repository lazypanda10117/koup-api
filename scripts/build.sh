#!/usr/bin/env bash
flask db init
flask db migrate
flask db upgrade
gunicorn -b 0.0.0.0:3000 app:app