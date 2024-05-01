a = ['Gfg', 'is', 'best', 'for', 'Geeks']
"""while True:
    b = input("enter the word one by one")
    print("For stop just prees enter")
    if b == "":
        break
    else:
        a.append(b)"""
c = input("enter the 1st leeter")
d = input("enter the second second letter")
e = []
for i in a:
    i = i.replace(c, d)
    i = i.replace(d, c)
   # print(i.replace("G", "e"))
    e.append(i)
print(e)