
c = []
d = []
m = int(input("enter the 1st number"))
n = int(input("enter the last number"))
for i in range(m, n):
    if i % 2 == 0:
        c.append(i)
    else:
        d.append(i)
print(c)
print(d)
print(len(c))#it's just len of the even
print(len(d))#it's just len of odd
