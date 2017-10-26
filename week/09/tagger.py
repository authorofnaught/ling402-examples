#!/usr/bin/python3

import nltk
from nltk.corpus import brown
from collections import defaultdict

def get_tagger(train_sents, N, universal):
    """ Returns an N-gram tagger"""
    defaultTag = "NOUN" if universal else "NN"
    t0 = nltk.DefaultTagger(defaultTag)
    if N == 1:
        # unigram tagger with backoff
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        return t1
    elif N == 2:
        # bigram tagger with backoff
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        t2 = nltk.BigramTagger(train_sents, backoff=t1)
        return t2
    elif N == 3:
        # trigram tagger with backoff
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        t2 = nltk.BigramTagger(train_sents, backoff=t1)
        t3 = nltk.TrigramTagger(train_sents, backoff=t2)
        return t3
    else:
        print("returning default tagger")
        return t0



def main():

    while True:
        N = input("Enter the value of N. (0-3): ")
        if N.isdigit() and int(N) in [0,1,2,3]:
            N = int(N)
            break
        print("Response should be an integer between 0-3")

    while True:
        useUniv = input("Use universal tagset? (y/n)")
        if useUniv in ['y','n']:
            useUniv = True if useUniv == 'y' else False
            break
        print("Response must be y or n")

    while True:
        doUnk = input("Replace lower frequency words with UNK? (y/n): ")
        if doUnk in ['y','n']:
            doUnk = True if doUnk == 'y' else False
            while True:
                minFreq = input("Enter a minimum frequency for a word to be known: ")
                if minFreq.isdigit():
                    minFreq = int(minFreq)
                    break
                print("Response should be an integer value")
            break
        print("Response must be y or n")

    # use universal tagset if specified
    if useUniv:
        tagged_sents = brown.tagged_sents(categories='news', tagset='universal')
    else:
        tagged_sents = brown.tagged_sents(categories='news')

    # replace tokens of freq < minFreq with 'UNK'
    if doUnk:
        mapping = defaultdict(lambda: 'UNK')
        words = brown.words(categories='news')
        freqdist = nltk.FreqDist(words)
        mostfreq = [w for w in freqdist if freqdist[w] >= minFreq]
        for w in mostfreq:
            mapping[w] = w
        new_tagged_sents = []
        for tagged_sent in tagged_sents:
            new_tagged_sent = [(mapping[word], tag) for (word, tag) in tagged_sent]
            new_tagged_sents.append(new_tagged_sent)
        tagged_sents = new_tagged_sents

    size = int(len(tagged_sents) * 0.9)
    train_sents = tagged_sents[:size]
    test_sents = tagged_sents[size:]

    tagger = get_tagger(train_sents, N, useUniv)
    accuracy = tagger.evaluate(test_sents)
    print("Acc:\t{}".format(accuracy))


if __name__ == '__main__':
    main()
