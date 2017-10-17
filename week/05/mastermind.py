#!/usr/bin/python3

# plays a game of mastermind: the user must guess the random word

import os
import random
import sys


os.system('clear')

# swadesh is an easy dataset from which to choose a 
# single word at random
swadesh="/usr/share/nltk_data/corpora/swadesh/en"

lines = open(swadesh).read().split('\n')	
word = ""

while True:
	word = random.choice(lines)
	if len(word) > 0 and "(" not in word:
		break

###### DEBUG WORD ####
#word="hurrah"
######################

while True:
	guess = input("Guess a {}-letter word: ".format(len(word)))

	if guess == "":
		print("Giving up? The word was {}".format(word))
		sys.exit()
#### FOR DEBUGGING ####
#	elif guess == "?":
#		print(word)
#######################
	elif len(guess) != len(word):
		print("That is not a {}-letter word.".format(len(word)))
	elif guess == word:
		print("Correct!")
		sys.exit()
	else:
		num_correct = 0
		correct_pos = 0
		word_chars = list(word)
		for c in guess:
			if c in word_chars:
				num_correct+=1
				word_chars.remove(c)
		for i in range(len(guess)):
			if word[i] == guess[i]:
				correct_pos+=1
		print("{} out of {} letters correct".format(num_correct, len(word)))
		print("{} letters in the correct position".format(correct_pos))
		
