a = input("enter the string")
b = input("enter the second string which you want to compare")
c = len(a)
print(c)
n = 0
for i in a:
    if i in b:
        n = n + 1
if n >= c:
    print("both are same")