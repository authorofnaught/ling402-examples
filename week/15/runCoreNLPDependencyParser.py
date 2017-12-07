#!/usr/bin/python3

from nltk.parse.corenlp import CoreNLPDependencyParser, CoreNLPParser
from nltk.parse import DependencyGraph


con_parser = CoreNLPParser(url='http://localhost:9000')
dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')

def parse(sent):
    con_parse, = con_parser.raw_parse(sent)
    dep_parse, = dep_parser.raw_parse(sent)

    print()
    print("Constituency Tree:")
    con_parse.pretty_print()

    dg = DependencyGraph(dep_parse.to_conll(4))
    print()
    print("Dependency Tree:")
    dg.tree().pprint()

    print()
    print("Dependencies:")
    for governor, dependency, dependent in dg.triples():
        print(governor, dependency, dependent)

parse("The quick brown fox jumps over the lazy dog.")

while True:
    print()
    print()
    print("#############################################")
    print()
    sent = input("Enter the next sentence to parse:\n")
    parse(sent)
