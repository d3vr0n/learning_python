# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:27:29 2020

@author: achara6
"""

def announce(f):
    def wrapper():
        print("running announc wrapper >>")
        f()
        print(">> done running announce wrapper")
    return wrapper

@announce
def print_hello():
    print("Hello World")
    
    
print_hello()