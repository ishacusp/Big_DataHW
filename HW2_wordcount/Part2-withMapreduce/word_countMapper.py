word_countMapper.py

#!/usr/bin/env python
"""
Mapper Function - wrriten in Python 2
"""
import sys
dictionary = {"hackathon":0, "Dec":0, "Chicago":0, "Java":0}
for line in sys.stdin:
        line = line.strip()
        line = line.lower()
        for word in dictionary.keys():
            if word.lower() in line:
                print"%s\t%s" % (word, 1)

