#!/bin/bash
set -e

OAREPO_VERSION=${OAREPO_VERSION:-11}
OAREPO_VERSION_MAX=$((OAREPO_VERSION+1))

BUILDER_VENV=".venv-builder"
#if test -d $BUILDER_VENV ; then
#	rm -rf $BUILDER_VENV
#fi
#
#python3 -m venv $BUILDER_VENV
. $BUILDER_VENV/bin/activate
#pip install -U setuptools pip wheel
#pip install -e .


MODEL="thesis"
VENV=".venv-tests"

if test -d ./build-tests/$MODEL; then
	rm -rf ./build-tests/$MODEL
fi

if test -d ./$VENV; then
	rm -rf ./$VENV
fi

oarepo-compile-model ./build-tests/$MODEL.yaml --output-directory ./build-tests/$MODEL -vvv
python3 -m venv $VENV
. $VENV/bin/activate
pip install -U setuptools pip wheel
pip install "oarepo>=$OAREPO_VERSION,<$OAREPO_VERSION_MAX"
pip install "./build-tests/${MODEL}[tests]"
pytest build-tests/$MODEL/tests