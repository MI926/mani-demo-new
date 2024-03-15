a = input("enter the parta")
def firstlast(a):
    
        s = a.split(" ")
        k = ""
        print(s)
        for i in s:
            first = i[0].upper()
            

            b = i[0].upper() + i[1:-1] + i[-1].upper()
            k = k + " " + b
            if k == " " :
                k = ""

            print(b)
        print(k.lstrip())
firstlast(a)