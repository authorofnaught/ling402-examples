#!/usr/bin/python3

from random import randint

def roll():
	roll = randint(1,20)
	if roll == 1:
		print("Critical failure!")
	elif roll == 20:
		print("Critical hit!")
	else:
		print("You rolled {}.".format(roll))


if __name__ == '__main__':
	for i in range(100):
		roll()

