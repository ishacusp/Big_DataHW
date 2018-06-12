#!/usr/bin/env python

"""
This program takes the input and stores the output links in dictionary 3, and the PR values in the dictionary 2. 
It calculates "PR = PR/number of outlinks". It then outputs - outlink target, source page, PR and 
the original outlinks information (in a separate line) for each source page (read from the input).


"""
import sys

dictionary = {'A':2,'B':3,'C':2,'D':5,'E':1,'F':2}
dictionary2 = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
dictionary3 = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0} 
dictionary4 = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}

lis_input =[]

for line in sys.stdin:
    line = line.strip()
    lis_input.append(line.split(" "))

for i in lis_input:
    key = i[0]
    dictionary2[key] = round(float(float(i[-1])/dictionary[key]),8)
    dictionary3[key] = i[1:-1]
    for key_look in dictionary4:
        if key_look in dictionary3[key]:
            print key_look, "%s %s" % (key, dictionary2[key])
            
    print key," ".join(dictionary3[key])   

