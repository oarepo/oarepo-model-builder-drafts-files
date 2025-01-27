#!/bin/bash
set -e

OAREPO_VERSION=${OAREPO_VERSION:-12}
export PIP_EXTRA_INDEX_URL=https://gitlab.cesnet.cz/api/v4/projects/1408/packages/pypi/simple
export UV_EXTRA_INDEX_URL=https://gitlab.cesnet.cz/api/v4/projects/1408/packages/pypi/simple

BUILDER_VENV=".venv-builder"
MODEL="thesis"
VENV=".venv-tests"

if test -d $BUILDER_VENV ; then
	rm -rf $BUILDER_VENV
fi

if test -d ./build-tests/$MODEL; then
	rm -rf ./build-tests/$MODEL
fi

python3 -m venv $BUILDER_VENV
. $BUILDER_VENV/bin/activate
pip install -U setuptools pip wheel
pip install -e .

oarepo-compile-model ./build-tests/$MODEL.yaml --output-directory ./build-tests/$MODEL -vvv

if test -d ./$VENV; then
	rm -rf ./$VENV
fi

python3 -m venv $VENV
. $VENV/bin/activate
pip install -U setuptools pip wheel
pip install "oarepo[tests,rdm]==${OAREPO_VERSION}.*"
pip install "./build-tests/${MODEL}[tests]"

pytest build-tests/$MODEL/tests

pytest tests