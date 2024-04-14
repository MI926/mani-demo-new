from re import I


u = ""
v = input("Enter the string")
x = input("Enter the string: ") 
y = list(x)
z = list(v)

for i in x:
    for j in v:
        if j == i:
            #print(i, "It is not appceptable")
            pass
        else:
            u = u + i
print(u)                