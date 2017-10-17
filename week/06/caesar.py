#!/usr/bin/python3

import sys
from string import ascii_lowercase, ascii_uppercase

# lower = 97-122
# upper = 65-90

def shift_letter(char, shift):
	if char in ascii_lowercase:
		return chr((((( ord(char) - 97 ) + shift ) % 26 ) + 97 ))
	if char in ascii_uppercase:
		return chr((((( ord(char) - 65 ) + shift ) % 26 ) + 65 ))
	else:
		return char
	
def caesar(message, shift=None, decode=False):
	if shift:
		shift = int(shift)
		if decode:
			shift = -shift	
		print(''.join([shift_letter(c, shift) for c in message]))
	else:
		for i in range(26):
			print(''.join([shift_letter(c, i) for c in message]))


if __name__ == '__main__':
	if len(sys.argv) > 3:
		caesar(sys.argv[1], sys.argv[2], sys.argv[3])
	elif len(sys.argv) > 2:
		caesar(sys.argv[1], sys.argv[2])
	elif len(sys.argv) > 1:
		caesar(sys.argv[1])
	else:
		print("Usage: {} message [shift] [decode boolean]".format(sys.argv[0]))

