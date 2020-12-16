#!/bin/bash

if [ -d "venv" ]
then
    source venv/bin/activate
else
    python3 -m venv venv
    source venv/bin/activate
fi

if [ -f requirements.txt ]
then
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
fi

# deactivate

# python3 wsgi.py

# pip freeze | grep -v "pkg-resources" > requirements.txt
