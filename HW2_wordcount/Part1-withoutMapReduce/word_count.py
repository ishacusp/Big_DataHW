#!/usr/bin/env python

"""
This file (written in Python 3) counts the number of lines containing the word (words are passed through the dictionary)
"""
import sys
dictionary = {"hackathon":0, "Dec":0, "Chicago":0, "Java":0}
lines = [line.lower() for line in sys.stdin]
for line in lines:
    for word in dictionary:
        if word.lower() in line:
           dictionary[word]+=1

for i in dictionary:
    print(i, dictionary[i])








    
     

