a = input("Enter a string: ")
k = a.split(" ")
e = ""
for i in k:
    
    b = len(i)//2
    s = i[:b + 1].upper() + i[b:]
    print(s)
    e = e + " " + s
print(e.lstrip())    
def half_string(str):
    pass