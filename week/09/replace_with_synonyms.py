#!/usr/bin/python3

from nltk.corpus import wordnet as wn
from nltk.corpus import udhr
import sys, nltk

def main():
    text = udhr.raw('English-Latin1').lower()
#    text = "How now brown cow?"
    for sent in text.split('\n'):
        tokens = nltk.word_tokenize(sent)
        new_text = ""
        for token in tokens:
            foundSynonym = False
            for synset in wn.synsets(token):
                for lemma in synset.lemmas():
                    if lemma.name() != token:
                        new_text+=lemma.name()+' '
                        foundSynonym = True
                        break
                if foundSynonym:
                    break
            if not foundSynonym:
                new_text+=token+' '
        print(new_text)

if __name__ == '__main__':
    main()
