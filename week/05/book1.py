#!/usr/bin/python3

from nltk.book import *
from nltk import FreqDist

sents = [sent1, sent2, sent3, sent4, sent5, sent6, sent7, sent8, sent9]
texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9]

def no17():
	print(text9.index('sunset'))

def no18():
	vocab = []
	for s in sents[:7]:
		vocab += s
	vocab = sorted(set(vocab))
	print(vocab)
	
def no28(word, text):
	fdist = FreqDist(text)
	count = fdist[word]
	print((count/len(text)) * 100)
	
	

if __name__ == '__main__':
	no17()
	no18()
	no28('and', text6)
