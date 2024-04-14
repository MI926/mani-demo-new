x = input("Enter the string: ")
y = list(x)
w = 0
for i in x:
    z = i.isdigit()
    if z == True:
        w = w + 1
print(w)