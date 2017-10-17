#!/bin/bash

# plays a game of mastermind: the user must guess the random word

clear 

# swadesh is an easy dataset from which to choose a 
# single word at random
swadesh="/usr/share/nltk_data/corpora/swadesh/en"

WORD_SRC=${swadesh}

while true; do
	word=`shuf -n1 ${WORD_SRC}`
	if [[ $word =~ .*[()].* ]]; then
		continue
	else
		break
	fi
done

###### DEBUG WORD ####
#word="hurrah"
######################

while true; do

	read -p "Guess a ${#word}-letter word: "

	if [[ $REPLY == "" ]]; then
		echo "Giving up?  The word was ${word}"
		exit 0
	elif ! [[ ${#word} == ${#REPLY} ]]; then
		echo "That is not a ${#word}-letter word."
		continue
	elif [[ $REPLY == $word ]]; then
		echo "Correct!"
		exit 0
	else
		num_correct=0
		correct_pos=0
		unset chars
		for c in `echo $word | grep -o .`; do chars+=(${c}); done
		for (( i=0; i<${#word}; i=i+1 )); do
			for j in `echo ${!chars[@]}`; do
				if [[ ${chars[${j}]} == ${REPLY:${i}:1} ]]; then
					unset chars[${j}]
					((num_correct++))
					break 
				fi
			done
			if [[ ${word:${i}:1} == ${REPLY:${i}:1} ]]; then
				((correct_pos++))
			fi
		done
		echo "${num_correct} out of ${#word} letters correct."
		echo "${correct_pos} letters in the correct position"
	fi
done
