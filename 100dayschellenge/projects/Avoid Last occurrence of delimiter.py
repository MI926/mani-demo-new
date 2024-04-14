x = input("Enter the string: ")
y = list(x)
z = ""
k = 0
for i in y:
    if k == 0:
        z = z + i
    else:
        z = z + "*" + i 
    k = k + 1
print(z)    