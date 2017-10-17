#!/usr/bin/python3

from urllib import request
import re

url = "http://computational.linguistics.illinois.edu/ling402/Fall2017/index.html"
#url = "http://computational.linguistics.illinois.edu/ling402/Fall2017/schedule.html"

html = request.urlopen(url).read().decode('utf8')

pattern = re.compile(r"<([^!/\s>]+) ([^>]+)>")
attr_pattern = re.compile(r'([^\s=]+)=(".+")')

matches = re.finditer(pattern, html)

tagdict = {}

for match in matches:
    grouping = match.groups()
    tag = grouping[0]
    attr_string = grouping[1]
    if not tag in tagdict.keys():
        tagdict[tag] = []

    attr_dict = {}
    attrs = re.finditer(attr_pattern, attr_string)
    for attr in attrs:
        attr_grouping = attr.groups()
        attr_name = attr_grouping[0]
        attr_value = attr_grouping[1]
        attr_dict[attr_name] = attr_value
    tagdict[tag].append(attr_dict)
for key in tagdict.keys():
    print('tag =',key+'\t'+'count =',len(tagdict[key]))
    for i in tagdict[key]:
        print('\t',i)
