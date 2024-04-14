d = input("enter the string")
a = sorted(d)
b = len(a)
c = ""
for i in a:
    b = b - 1
    c = c + a[b]
print(c)