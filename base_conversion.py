# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:07:01 2015

@author: Ashish

To convert a give number (in decimal form) for a given base
"""

def base_convert(number,base):
    start = ""
    while number >= base:
        start = str(number%base) + start
        number = number/base
    start = str(number) + start
    
    return start

n = raw_input("Number? ")
number = int(n)
b = raw_input("Base? ")
base = int(b)

print base_convert(number,base)