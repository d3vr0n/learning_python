# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:11:37 2020

@author: achara6
"""

from collections import Counter

word1 = "abcc"
word2 = "cabc"

if Counter(word1) == Counter(word2):
 print("yes")
else:
 print("no")
 
print(Counter(word1))