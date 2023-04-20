#!/bin/bash

book="$(cut -d',' -f 1 data.csv | fzf)"

python3 main.py "$book" "$1"
