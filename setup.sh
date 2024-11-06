#!/bin/bash

# Exit script if any command fails
set -e

# Print each command before running it
set -x

# Set PYTHONPATH to the current directory
export PYTHONPATH=$(pwd)

# Run setup.py to build the package
python setup.py sdist bdist_wheel

# Install the package locally
pip install .

# Clean up build directories
rm -rf build/ dist/ *.egg-info

echo "Package built, installed, and cleaned up successfully."
