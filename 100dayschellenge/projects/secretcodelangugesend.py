import mpmath
from decimal import Decimal
import math
a = input("enter the message")
a = list(a)
b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

d = ""
for i in a:
    c = 0
    for j in b:
        if i == j:
            d = d + str(c)
            
        c = c + 1
print(d)
e = len(a)
print(int(d) / e)
print(float(math.log(int(d),e)))
f = mpmath.log(int(d), e) 
g = str(f) + "_" + str(e)
print(g)
k = 0
h = ""
for i in g:
    print(i)
    if i == "_":
        g[0:k]
        print(g)
        break
    h = h + i
    k = k + 1
print(k)
print(h)
i = g[k + 1:]
print(i)
antilog = Decimal(math.pow(Decimal(i), Decimal(h)))
print(antilog)


'''
g = f + "_" + str(e)
print(g)

j = float(h) * int(i)
print(j)

'''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            