#!/usr/bin/env python3
from collections import Counter
f = "The_Hunger_Games.txt"
lis=[]
with open(f, 'r') as content_file:
    content = content_file.read()
    for i in content.split():
        if i == i[::-1] and len(i)>2:
            lis.append(i)
lis.sort()
lis.pop(0)
fin=dict((x, lis.count(x)) for x in set(lis) if lis.count(x) > 1)
print(fin)
print(fin.keys())
