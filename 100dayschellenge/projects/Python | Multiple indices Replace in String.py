x = input("enter the string")
y = []
while True:
    a = int(input("enters the numbers one by one and at the end enter the negative number to stop the loop"))
    
    if a < 0:
   
        break
    else:
        y.append(a)
        



#y = int(input("enter the number of the word which you want to change"))
a = input("enter the word which you want to replace it with")
#z = list(y)
n = 0
k = ""
#print(z)
for i in x:
    print(i)
    if n in y:
        print(n)
        k = k + a
    else:
        k = k + i
    n = n + 1 
print(k)