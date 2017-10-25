#!/usr/bin/python3

from nltk.corpus import wordnet as wn
from nltk.corpus import udhr
import sys, nltk

def find_synonym(token):
    synsets = wn.synsets(token)
    for synset in synsets:
        for lemma in synset.lemmas():
            if lemma.name() != token:
                return lemma.name()
    return token

def main():
    text = udhr.raw('English-Latin1').lower()
#    text = "How now brown cow?"
    for sent in text.split('\n'):
        tokens = nltk.word_tokenize(sent)
        new_text = ""
        for token in tokens:
            new_text+=find_synonym(token)+' '
        print(new_text)

if __name__ == '__main__':
    main()
