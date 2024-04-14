x = input("enter the string")
y = input("enter the string")
z = list(x)
k = list(y)
aad = ""
num = 0
for m in z:
    for n in k:
        if m == n:
            print(m)
            aad = aad + m 
            num = num + 1
print(aad)
print(num)