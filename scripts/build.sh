#!/usr/bin/env bash
gunicorn -b 0.0.0.0:3000 app:app