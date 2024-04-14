a = input("enter the string")
b = a.split(" ")
n = 0
c = {}
for i in range(len(b)):
    d = n + 1
    if d < len(b):
        
        c[b[n]] = b[n + 1]
    n = n + 2
print(c)
