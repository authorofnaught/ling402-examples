#!/usr/bin/python3

import sys

word = "fish"


while True:

	guess = input("Guess a {}-letter word: ".format(len(word)))

	#begin comparison of word and guess
	if word == guess:
		print("Correct!")
		sys.exit()
	else:
		print("Your guess, {}, is incorrect.".format(guess))



print("This should not be printed")
