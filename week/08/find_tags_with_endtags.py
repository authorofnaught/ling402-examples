#!/usr/bin/python3

from urllib import request
import re

url = "http://computational.linguistics.illinois.edu/ling402/Fall2017/index.html"
#url = "http://computational.linguistics.illinois.edu/ling402/Fall2017/schedule.html"

html = request.urlopen(url).read().decode('utf8')

pattern = re.compile(r"<([^!/\s]+[^>]*)>.+</\1>")

matches = re.finditer(pattern, html)

tags = []

for match in matches:
    matchstring = match.group(0)
    tags.append(matchstring)

for tag in set(tags):
    print(tag)
