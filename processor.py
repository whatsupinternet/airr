#!/usr/bin/env python

results = []
with open('nouns.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(','))
results = map(lambda x: x[0], results)
results = [word for word in results if len(word) <= 6 and len(word) >= 3]
print results 
