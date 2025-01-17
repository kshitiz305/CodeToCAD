#!/usr/bin/env bash

rm -rf ./dist/*
python setup.py sdist bdist_wheel
twine check dist/*
twine upload -r pypi dist/* --config-file ./.pypirc --verbose