#!/usr/bin/python3

from urllib import request
import re

url = "http://computational.linguistics.illinois.edu/ling402/Fall2017/"
#url = "http://computational.linguistics.illinois.edu/ling402/Fall2017/schedule.html"

html = request.urlopen(url).read().decode('utf8')

pattern = re.compile(r"<([^!/>\s]+)>")

matches = re.findall(pattern, html)

tagnames = []

for match in matches:
    tagnames.append(match)

for tagname in set(tagnames):
    print(tagname)
