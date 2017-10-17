#!/bin/bash

#prompts the user to guess a random number correctly

clear 

upper_limit=1000
num_guesses=10
number=$(( RANDOM % $upper_limit ))

while [[ $num_guesses > 0 ]]; do

	echo "You have ${num_guesses} guesses remaining..."
	read -p "Guess a number between 0 and ${upper_limit}: "

	if [[ $REPLY == "" ]]; then
		echo "Giving up? The number was ${number}."
		exit 0
	fi

	if ! [[ $REPLY =~ ^[0-9]+$ ]]; then
		echo "That's not a number.  Check your keyboard."
		continue
	fi

	if [[ $REPLY -eq $number ]]; then
		echo "Correct!"
		exit 0
	elif [[ $REPLY -gt $number ]]; then
		echo "Too high..."
	elif [[ $REPLY -lt $number ]]; then
		echo "Too low..."
	else
		echo "something went wrong. exiting..."
		exit 1
	fi

	num_guesses=$(( num_guesses - 1 ))

done

echo "Too bad.  The number was ${number}."

