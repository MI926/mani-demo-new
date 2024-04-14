a = input("enter the string")
b = a.split(" ")
c = input("enter the word")
e = []
for i in b:
    d = len(i)
    if i[d - 1] == c:
        pass
    else:
        e.append(i)
print(e)
