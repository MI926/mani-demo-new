a = input("enter the string")
b = input("enter the word to replacee")
c = input("enter word by replacwe")
d = a.split(" ")
e = b.split(" ")
f = ""
for i in d:
    if i in e:
        f = f + " " + c
        continue
    f = f + " " + i
print(f)