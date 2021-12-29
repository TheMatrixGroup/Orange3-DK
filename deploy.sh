#!/bin/bash
rm -rf build/* dist/* Orange3_DK.egg-info/*
python -m build
# python -m twine upload --repository testpypi dist/*
python -m twine upload dist/*