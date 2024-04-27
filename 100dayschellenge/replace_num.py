print("1st value is for nuber you want to replace.       2nd Value is for number to replace")
def replacefun(b, d):
    a = [1, 234, 65, 56, 436, 7456]

    c = []
    for i in a:
        if i == b:
            c.append(d)
        else:
            c.append(i)
    print(c)
    
b = int(input("Enter the number which you want to replace"))
d = int(input("Enter the number which can replace"))
replacefun(b, d)