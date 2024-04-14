from math import e
from secrets import randbelow


x = input("Enter the string: ")
y = input("Enter the number: ")
o = ""

for i in range(0, len(x) + 1 ):
    a = x[i:] + x[:i]
    print(a)
    if a == y:
            
            o = i
            
print(o)