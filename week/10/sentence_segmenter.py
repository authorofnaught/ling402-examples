#!/usr/bin/python3

import nltk, sys


def punct_features(tokens, i):
#    return {'punct': tokens[i]
#            }
    return {'next-word-capitalized':tokens[i+1][0].isupper(),
            'prev-word':tokens[i-1].lower(),
            'punct':tokens,
            'prev-word-is-one-char':len(tokens[i-1]) == 1
            }

sents = nltk.corpus.treebank_raw.sents()
tokens = []
boundaries = set()
offset = 0
for sent in sents:
    tokens.extend(sent)
    offset += len(sent)
    boundaries.add(offset-1)

featuresets = [(punct_features(tokens, i), (i in boundaries))
        for i in range(1, len(tokens)-1)
        if tokens[i] in '.?!']

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
#classifier = nltk.NaiveBayesClassifier.train(train_set)
classifier = nltk.DecisionTreeClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))

def segment_sentences(words):
    start = 0
    sents = []
    for i, word in enumerate(words):
        if word in '.?!' and classifier.classify(punct_features(words, i)) == True:
            sents.append(words[start:i+1])
            start = i+1
    if start < len(words):
        sents.append(words[start:])
    return sents

#text = sys.stdin.read()
for line in sys.stdin:
    words = nltk.word_tokenize(line.strip())+[" "]
    sents = segment_sentences(words)
    print(sents)


