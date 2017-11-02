#!/usr/bin/python3

import nltk, sys

#################################################
# This script will print out accuracy on the test 
# set and then sgement text from stdin into 
# sentences.
#################################################


# Features
#################################################
def punct_features(tokens, i):
    features = {}
    features['punct'] = tokens[i]
    return features
#################################################

sents = nltk.corpus.treebank_raw.sents()
tokens = []
boundaries = set()
offset = 0
for sent in sents:
    tokens.extend(sent)
    offset += len(sent)
    boundaries.add(offset-1)

# We are obtaining features for each .?! in the 
# corpus, and then we will decide whether that 
# token indicates a sentence boundary.
#################################################
featuresets = [(punct_features(tokens, i), (i in boundaries))
        for i in range(1, len(tokens)-1)
        if tokens[i] in '.?!']
#################################################

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
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

text = sys.stdin.read().strip()
text = text.replace('.', ' . ')
text  = text.replace('?', ' ? ')
text  = text.replace('!', ' ! ')
words = text.split()+[" "]
sents = segment_sentences(words)
for sent in sents:
    print(' '.join(sent))



