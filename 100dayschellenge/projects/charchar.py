x = input("Enter the string: ")
y = list(x)
u = input("Enter the string: ")
a = ""
for i in y:
    if i in u:
       print(x, "It is not appceptable")
       break
        
        
    else :
        a = a + i