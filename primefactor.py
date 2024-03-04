x = int(input("enter the number :- "))

for i in range(1,x+1):
    while x % i == 0:
        #print(i)
        for a in range(2,i+1):
            if i % a == 0:
                break
            else:
                print(i)
                break
            
        x = x / i
        if i == 1 or i == 0:
            i = i + 1
        if x % 2 == 0:
            print(2)