#!/usr/bin/python3

import nltk, sys, random
from nltk.corpus import names
from nltk.classify import apply_features

def gender_features(name):
    features = {}
    features['last_letter'] = name[-1].lower()
    features['last_two_letters'] = name[-2:].lower()
    return features

labeled_names = ([(name, 'male') for name in names.words('male.txt')] + 
                   [(name, 'female') for name in names.words('female.txt')]) 

random.shuffle(labeled_names)

featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
#train_set, test_set = featuresets[500:], featuresets[:500]
train_names = labeled_names[1500:]
devtest_names = labeled_names[500:1500]
test_names = labeled_names[:500]
train_set = apply_features(gender_features, train_names)
dev_set = apply_features(gender_features, devtest_names)
test_set = apply_features(gender_features, test_names)
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, dev_set))
print(nltk.classify.accuracy(classifier, test_set))
print(classifier.show_most_informative_features(10))

errors = []
for (name, tag) in devtest_names:
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append( (tag, guess, name) )

for (tag, guess, name) in sorted(errors):
    print("correct={:<8} guess={:<8s} name={:<30}".format(tag, guess, name))


