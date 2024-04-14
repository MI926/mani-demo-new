x = input("Enter the string: ")
a = 0
o = []
for i in x:
    e = [(i, x.count(i))]
    o.extend(e)
j = ""    
for i in o:
    if 0 != i[1] % 2:
        j = j + i[0]
    
print(j)
        