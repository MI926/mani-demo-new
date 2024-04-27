num = int(input("enter the numbe"))
b = str(num)
print(b)
c = 0
d = ""
for i in b:
    e = len(b) - c - 1
    d = d + b[e]
    c += 1
    
print(d)