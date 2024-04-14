a = input("enter the string")
b = input("enter the  which you want to replaca")
c = input("enter the word which can replace")
d = ""
e = list(b)
f = []
n = 0
for i in b:
    print(n)
    g = (i, c[n])
    f.append(g)
    n = n + 1
print(f)



for i in a:
    print(i)
    for j in f:
        if i == j[0]:
            

           a = a.replace(i, j[1])

           
            
    
print(a)
