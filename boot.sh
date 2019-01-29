#!/bin/sh

. venv/bin/activate
cd app
exec gunicorn --config ../gunicorn-config.py alfieweb:app
