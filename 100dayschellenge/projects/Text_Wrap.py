'''x = input("enter the paragraph :- ")
z = int(input("enter the number :- "))
for i in range(1, len(x)):
    y = z * i
    m = z * (i - 1)
    k = [x[m:y]]
    c = x.__len__()
    if c - y <= 4:
        break
    print(k)'''
'''import textwrap 
  
value = input("enter the paragraph :- ") 
x = int(input())
  
# Wrap this text. 
wrapper = textwrap.TextWrapper(width=x) 
  
string = wrapper.fill(text=value) 
  
print (string) '''
import textwrap

def wrap(string, max_width):
    value = string
    x = max_width
  
    # Wrap this text. 
    wrapper = textwrap.TextWrapper(width=x) 
  
    string = wrapper.fill(text=value) 
  
    print (string)
    b = len(string)
    if b <= 0:
        return


    return

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ