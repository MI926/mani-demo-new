import copy
a = input("Enter the list number without space")
#b = input("Enter the number which you want to find")
#c = a.find(a)
print(list(a))
a = list(a)
a.sort()
print(a)
b = len(a)
print(b)
c = []
d = []
for i in a:
    i = int(i)
    if i % 2 == 0:
        
        c.append(i) 
    else:
        d.append(i)
print(c)#this is the even number list
print(d)
print(len(c))
print(len(d))