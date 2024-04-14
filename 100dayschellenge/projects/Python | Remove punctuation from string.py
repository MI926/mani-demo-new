a = input("enter the string")
b = []
c = input("enter the word which you want to remove")
d = ""
for i in c:
    b.append(i)
print(b)
for i in a:
   if i in b:
       pass
   else:
       d = d + i
print(d)