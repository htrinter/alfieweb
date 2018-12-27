#!/bin/sh

. venv/bin/activate
cd app
exec gunicorn -b :5000 --access-logfile - --error-logfile - alfieweb:app
