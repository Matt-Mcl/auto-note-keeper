#!/bin/bash

directory=$1

source "$directory/venv/bin/activate"

python3 "$directory/main.py"
