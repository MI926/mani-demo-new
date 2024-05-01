a = []
while True:
    b = input("enter the word one by one")
    print("For stop just prees enter")
    if b == "":
        break
    else:
        a.append(b)
c = int(input("enter the 1st elemnt's index"))
d = int(input("enter the second element's index"))
e = a[c]
print(a)
f = a[d]
a[c] = f
a[d] = e
print(a)