#!/usr/bin/env python
"""
This program takes in the output from the mapper program, splits the input by spaces.
It then retrieives the value at the last index for each arraylist in the list 'linered'. If the value is a
number, then it adds this numeric value (PR) in dictionary_red for the particular matching key. 
Otherwise, it stores the entire array list (except the value at the 0th index - as it is stored as a key)
as values for the same key in the dictionary_red1 (output links of the original page).
Lastly it just output the Page, the outlinks, and the new PR values in the same format as the input file.

"""

import sys

#This function checks if a input argument is a number or not. 
#Fetched from: https://www.pythoncentral.io/how-to-check-if-a-string-is-a-number-in-python-including-unicode/

def is_number(s): 
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


lis_inputred = []


for linered in sys.stdin:
    linered  = linered.strip()
    lis_inputred.append(linered.split(" "))

    
dictionary_red = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0}
dictionary_red1 = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0}
for i in lis_inputred:
    key = i[0]
    if(is_number(i[-1])):
        for key_look in dictionary_red:
             if key_look ==key:
                dictionary_red[key_look] = round(dictionary_red[key_look]+ float(i[-1]),8)
        
    else: dictionary_red1[key] = i[1:]
                                                 
            
for key_print in dictionary_red:
    print key_print,"%s %s" % (" ".join(dictionary_red1[key_print]), dictionary_red[key_print])  
