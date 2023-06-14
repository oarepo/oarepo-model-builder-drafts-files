#!/bin/bash
set -e

MODEL="thesis"
VENV=".model_venv"

if test -d ./build-tests/$MODEL; then
	rm -rf ./build-tests/$MODEL
fi
if test -d $VENV ; then
	rm -rf $VENV
fi

oarepo-compile-model ./build-tests/$MODEL.yaml --output-directory ./build-tests/$MODEL -vvv
python3 -m venv $VENV
. $VENV/bin/activate
pip install -U setuptools pip wheel
pip install "./build-tests/$MODEL[tests]"
pytest build-tests/$MODEL/tests