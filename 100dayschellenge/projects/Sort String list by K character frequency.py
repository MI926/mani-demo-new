x = input("Enter the string: ")
y = input("Enter the letter: ")

z = x.split(" ")
w = {}
for i in z:
    print(i)
    for j in i:
        print(j)
        a = i.count(y)
        print(a)
        b = (a, i)
        w[b] = ""
print(w)
v = []
'''for i in w:
    print(i)
    c = i[0]
    c.sort()
    for j in range (0, max(c)):
        if i[0] == c[j]:
            v.append(i)
print(v) '''
print(sorted(w, key=lambda num: num[0])) 
# i dont know the above expression
