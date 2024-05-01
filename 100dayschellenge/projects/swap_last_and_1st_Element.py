a = []
while True:
    b = input("enter the word one by one")
    print("For stop just prees enter")
    if b == "":
        break
    else:
        a.append(b)
print(a)
c = len(a) - 1
d = a[c]
e = a[0]
a[0] = d
a[c] = e
print(a)