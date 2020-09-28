# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:33:29 2020

@author: achara6
"""

people = [{"Name": "A", "Age":28},
          {"Name": "C", "Age":29},
          {"Name": "B", "Age":27}
          ]


def sort_name(person):
    return person["Name"]

people.sort(key=sort_name)

print(people)

# lambda function

people.sort(key= lambda person: person["Age"])
print(people)