#!/usr/bin/python3

from nltk.corpus import wordnet as wn
from nltk.corpus import udhr
import sys, nltk

def find_synonym(token, tag):
    synsets = []
    # noun
    if tag.startswith('N'):
        synsets += wn.synsets(token, pos='n')
    # verb
    elif tag.startswith('V'):
        synsets += wn.synsets(token, pos='v')
    # abverb
    elif tag.startswith('R'):
        synsets += wn.synsets(token, pos='r')
    # adjective
    elif tag.startswith('J'):
        synsets += wn.synsets(token, pos='a')
        synsets += wn.synsets(token, pos='s')
    # other, in case wn contains synsets for the token
    # wn.synsets returns [] if token belongs to no synsets
    else:
        synsets += wn.synsets(token)

    for synset in synsets:
        for lemma in synset.lemmas():
            if lemma.name() != token:
                return lemma.name()
    return token

def main(text):
    for sent in text.split('\n'):
        tokens = [token.lower() for token in nltk.word_tokenize(sent)]
        tokens = nltk.pos_tag(tokens)
        new_text = ""
        for token, tag in tokens:
            new_text+=find_synonym(token, tag)+' '
        print(new_text)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main(udhr.raw('English-Latin1'))
