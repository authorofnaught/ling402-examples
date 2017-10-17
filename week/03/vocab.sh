#!/bin/bash

# reads a file from stdin and calculates the type/token ratio
words=$(sed 's/[[:punct:]]//g' | tr ' ' '\n' | tr -s '\n' | sort)
num_total_words=$(echo "$words" | wc -l | cut -f1 -d' ')
num_uniq_words=$(echo "$words" | uniq | wc -l | cut -f1 -d' ')
echo "num_uniq = ${num_uniq_words}"
echo "num_total = ${num_total_words}"
python3 -c "print(${num_uniq_words}/${num_total_words})"
