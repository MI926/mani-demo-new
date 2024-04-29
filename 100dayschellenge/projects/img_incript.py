import io
from PIL import Image
import base64
from imgbyte import byet_arry

 
# Open image using the pillow package
img = Image.open("100dayschellenge/wp5457083-780130089.jpg")
# initialiaze io to_bytes converter
img_byte_arr = io.BytesIO()
# define quality of saved array
img.save(img_byte_arr, format='JPEG', subsampling=0, quality=100)
# converts image array to bytesarray
img_byte_arr = img_byte_arr.getvalue()
a = base64.b64encode(img_byte_arr)
a = bytes(a)
#with open('100dayschellenge/projects/imgbyte.py', 'w') as file:
  #file.write("byet_arry =  ")
#with open('100dayschellenge/projects/imgbyte.py', 'a') as file:
  #file.write(str(a))
#how to convert the byte_ARRAY ti image.
#with open('100dayschellenge/projects/imgbyte.txt', 'r') as file:
 # b = file.read()
  #c = base64.b64decode(b)
  #print(c)
#b = base64.b64decode(byet_arry)
#c = Image.open(io.BytesIO(b))
#c.show()
print(len(a))
#import qrcode
 
# Data to be encoded
#data = 'QR Code using make() function'
 
# Encoding data using make() function
#img = qrcode.make(str(a)) 
 
# Saving as an image file
img.save('MyQRCode1.png')
with open('100dayschellenge/wp5457083-780130089.jpg', 'ab') as file:
  file.write(a)
with open('100dayschellenge/wp5457083-780130089.jpg', 'rb') as f:
  #d = f.read()
  #offset = content.index(bytes.fromhex('FFD9'))
  #f.seek(offset + 2)
  print(base64.b64encode(f.read()))
import cv2

print(cv2.__version__)
img = cv2.imread('data/src/qrcode.png')