a = input("enter the string with for different letter use space")
b = a.split(" ")
c = {}
for i in b:
    for j in i:
        if j == " ":
            pass
        else:
            c[i] = ""
            continue

print(c)
