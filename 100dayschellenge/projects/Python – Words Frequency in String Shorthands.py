x = input("Enter the string: ")
y = x.split(" ")
z = {}
b = 0
for i in y:

    a = x.count(i)
    #print(a)
    #print(i)
    if a >= 0:

        
        c = (a, i)
        z[c] = ""
    # print(i)
print(z)

