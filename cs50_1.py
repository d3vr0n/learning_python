# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:51:22 2020

@author: achara6
"""


n = int(input("Number: "))
if n>0:
    print(f"{n} is positive")
elif n<0:
    print(f"{n} is negative")
else:
    print(f"{n} is zero")
    
# create a set
s = set()

s.add(2)
s.add(3)
s.add(2)

print(s)

# dictionaries

person = {"Name":"A","Age":28}

person["Email"] = "test@test.cc"

print(person)
print(person["Name"])

# functions

def square(x):
    return x * x;

for i in range(10):
    print(f"Num: {i}, Sq: {square(i)}")