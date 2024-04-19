a = input("enter the message")
o = len(a)
print(a)
b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
     "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
     ",", ".", "?", "!", "@", "#", "$", "%", "^", "&", "*",
     "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/", " ", "-", "_", "+", "=", "(", ")", "[", "]", "{", "}", ":", ";", "'", "\"", "<", ">", "|", "~", "`",]


d = ""
c = len(a)
print(c)
e = len(b)
g = 0
print(e)
for f in range(0, c):
    if c > e:
        c = c - e
        #print("elsewala 1st", c)
    else:
        break
print(c)
f = 0
list1 = []
list2 = []
for i in a:
    #print(i)
    f = 0
    for j in b:
        if i == j:
           #print(i, "2")
            list1.append(f + c)
            list2.append(f)
        f = f + 1
print(list1)
print(list2, "orignal num")
print(len(list1))
k = []
for i in list1:
    l = 0 
    if int(i) > e:
        l = int(i) - e
        k.append(l)
        #print("elsewala 1st", c)
    else:
        k.append(i)
else:
    pass
print(k)
g = ""
for i in k :
    h = 0
    for j in b:
        if i == h:
            #print(j)
            g = g + j
        h = h + 1
print(g)

print(len(g))
m = str(g) + "_____" + str(o)
print(m)


# The variables a and v are not the same because:
# - a is the original input string 
# - v is the decoded output string after encrypting and decrypting a
# So v should match the original a, but they are not exactly the same variable.

