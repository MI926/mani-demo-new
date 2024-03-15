def onlyeven(a):
    s = a.split(" ")
    for i in s:
        if len(i)%2 == 0:
            print(i)
x = input("enter the parra  ")  
onlyeven(x)          