#!/bin/sh

python3 -m venv venv
venv/bin/pip install pip --upgrade
venv/bin/pip install setuptools --upgrade
venv/bin/pip install -r requirements.txt
. venv/bin/activate

cd app

export FLASK_ENV=development
export FLASK_APP=alfieweb.py
flask run
