a = input("enter the string")
b = input("enter the second string")
n = 0
for i in b:
    if i in a:
        n = n + 1
#for Python – Check if two strings are Rotationally Equivalent

"""if n >= len(a):
            print("both are same")
            
    else:
        print("both are not same")
        """
#print(n)
if len(b) == n and n < len(a):
    print("is subset")
    
else:
    print("not a sub")
   