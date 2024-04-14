x = input("Enter the string: ")
y = input("Enter the string: ")
z = list(x)
w = list(y)
v = []
u = []
for i in z:
    k = z.count(i)
    l = [(i, k)]
    v.extend(l)
for i in v:
    for a in w:

        if i[0] == a :
            #print(i)
            if i not in u:
                u.append(i)
print(u)                