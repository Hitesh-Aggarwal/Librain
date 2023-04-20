#!/bin/bash
echo "Enter number of suggestions: " 
read num
book="$(cut -d',' -f 1 data.csv | fzf)"
python3 main.py "$book" "$num"
