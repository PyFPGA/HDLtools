#!/bin/bash

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "ERROR: This script must be sourced to activate the environment."
    echo "Run it as: source ${0}"
    exit 1
fi

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

pip install --upgrade pip
pip install pyslang
pip install jinja2

# pip install -e .
SDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
export PYTHONPATH="${SDIR}:${PYTHONPATH}"
