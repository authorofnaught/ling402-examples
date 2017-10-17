#!/usr/bin/python3

import sys
from string import ascii_lowercase, ascii_uppercase

# lower = 97-122
# upper = 65-90

LOWER = [ord(c) for c in ascii_lowercase]
UPPER = [ord(c) for c in ascii_uppercase]

def str_2_ascii(text):
	ords = []
	for char in list(text):
		ords.append(ord(char))
	return ords

def ascii_2_str(ords):
	text = ""
	for o in ords:
		text+=chr(o)
	return text

def shift_letter(charOrd, shift):
	if charOrd in LOWER:
		return (((( charOrd - 97 ) + shift ) % 26 ) + 97 )
	elif charOrd in UPPER:
		return (((( charOrd - 65 ) + shift ) % 26 ) + 65 )
	else:
		return charOrd
	
def caesar(message, shift=None, decode=False):

	ords = str_2_ascii(message)

	if shift:
		shift = int(shift)
		if decode:
			shift = -shift	
		for i in range(len(ords)):
			ords[i] = shift_letter(ords[i], shift)
		shifted = ascii_2_str(ords)
		print(shifted)
	else:
		for n in range(26):
			for i in range(len(ords)):
				ords[i] = shift_letter(ords[i], 1)
			shifted = ascii_2_str(ords)
			print(shifted)


if __name__ == '__main__':
	if len(sys.argv) > 3:
		caesar(sys.argv[1], sys.argv[2], sys.argv[3])
	elif len(sys.argv) > 2:
		caesar(sys.argv[1], sys.argv[2])
	elif len(sys.argv) > 1:
		caesar(sys.argv[1])
	else:
		print("Usage: {} message [shift] [decode boolean]".format(sys.argv[0]))

