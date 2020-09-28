# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:57:02 2020

@author: achara6
"""

import sys

x = int(input("x: "))
y = int(input("y: "))

try:
    result = x/y
except ZeroDivisionError:
    print("Error: cannot divide by zero")
    sys.exit(1)
    
print(f"{x} / {y} = {result}")