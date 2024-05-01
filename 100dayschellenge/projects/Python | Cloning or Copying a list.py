import copy
a = input("Enter the list number without space")
#b = input("Enter the number which you want to find")
#c = a.find(a)
print(list(a))
a = list(a)
b = a[:]
print(b)
c = copy.copy(a)
print(c)