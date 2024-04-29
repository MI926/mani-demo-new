# Decode base64 encoded image back to bytes
import base64
import io
from PIL import Image
with open('100dayschellenge/wp5457083-780130089.jpg', 'rb') as f:
    img_data = base64.b64decode(f.read())

# Convert decoded bytes back to image  
img = Image.open(io.BytesIO(img_data))

# Save decoded image 
img.save('decoded_image.png')




import numpy as np
from pyzbar.pyzbar import decode
e = decode(Image.open("decoded_image.png"))
print(e[0].data.decode())

m = e[0].data.decode()
b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
     "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
     ",", ".", "?", "!", "@", "#", "$", "%", "^", "&", "*","0", "1",
     "2", "3", "4", "5", "6", "7", "8", "9", "/", " ", "-", "_", "+",
     "=", "(", ")", "[", "]", "{", "}", ":", ";", "'", "\"", "<", ">",
     "|", "~", "`",]



d = ""

e = len(b)
n = m.split("_____")
t = n[0]
p = int(n[1])
print(t)
print(p)
for f in range(0, p):
    if p > e:
        p = p - e
        #print("elsewala 1st", c)
    else:
        break
#print(c)
print(p)
q = int(e) - int(p)
print(q)
s = []
for i in t:
    r = 0
    for j in b:
        if i == j:
            s.append(r + q) 
        r = r + 1
u = [] 
for i in s:
    if int(i) > e - 1:
        x = int(i) - e
     
        u.append(x)
    else:
        u.append(i)
print(u)
print(len(u))
v = ""  
for i in u:
    w = 0
    for j in b:
        if i == w:
            v = v + b[w]
        w = w + 1
print(v)