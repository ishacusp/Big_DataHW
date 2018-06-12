word_countReducer.py

#!/usr/bin/env python

"""
Reducer function - written in Python 2
"""
import sys

dictionary = {"hackathon":0, "Dec":0, "Chicago":0, "Java":0}
for line in sys.stdin:
     word, count  = line.strip().split('\t')
     for i in dictionary:
         if i == word:
                dictionary[i]+=1

for i in dictionary:
        print"%s\t%s" % (i, dictionary[i])