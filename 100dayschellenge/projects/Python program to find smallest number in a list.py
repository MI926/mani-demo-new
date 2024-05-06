import copy
a = input("Enter the list number without space")
#b = input("Enter the number which you want to find")
#c = a.find(a)
print(list(a))
a = list(a)
a.sort()
print(a)
b = len(a) - 1
print(a[b:])#largest
print(a[0:1])#smallest
list1 = 
mx = max(list1[0], list1[1]) 
secondmax = min(list1[0], list1[1]) 
n = len(list1)
for i in range(2,n): 
    if list1[i] > mx: 
        secondmax = mx
        mx = list1[i] 
    elif list1[i] > secondmax and \
        mx != list1[i]: 
        secondmax = list1[i]
    elif mx == secondmax and \
        secondmax != list1[i]:
          secondmax = list1[i]
 
print("Second highest number is : ",\
      str(secondmax))