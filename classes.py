# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:13:40 2020

@author: achara6
"""

class Point():
    def __init__(self, input1 ,input2):
        self.x = input1
        self.y = input2
        

p = Point(2,8)
print(p)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)
        

flight = Flight(3)

people = ["pers1", "pers2", "pers3", "pers4"]
for p in people:
    suc = flight.add_passenger(p)
    if suc:
        print(f"Added passenger {p}")
    else:
        print(f"Rejected passenger {p}")
