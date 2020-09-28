import random

for x in range(0,random.randint(1,10)):
    print(x)

print('----------------')

person = {'Name':'Avi','Age':30}

for key in person:
    print (key, ": ", person[key])

print('----------------')

# Error handling

try:
    input = int( input("type a number") )
except:
    print("invalid number")
