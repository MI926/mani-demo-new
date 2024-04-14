x = input("Enter the string: ")
y = input("Enter the number: ")
z = list(x)
w = 0
for i in z:
    a = x.find(i)
    print(a)
    b = x[a:(a + 1)]
    print(b)
    if w + len(i) > y:
        
'''
 i just dont know the re module and i attempt it after video 99 code wuth harry
 '''    