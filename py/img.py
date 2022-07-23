#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys

with open(sys.argv[1]) as f:
    html = BeautifulSoup(f.read(), 'html.parser')


for i in html.find_all('p'):
    if len(i.find_all('img')) > 0:
        i.unwrap()

with open(sys.argv[1], 'w') as f:
    f.write(str(html))
