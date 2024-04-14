a = input("Enter the string")
b = ""
for i in a:
    c = a.count(i)
    if i not in b:
        
        if c > 1:
            b = b + i
print(b)