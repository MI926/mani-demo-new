a = input("enter the string")
b = list(a)
x = ""
for i in b:
    if i not in x:
        x = x + i
        
print(x)