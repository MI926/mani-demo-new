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
import textwrap 
  
value = input("enter the paragraph :- ") 
x = int(input())
  
# Wrap this text. 
wrapper = textwrap.TextWrapper(width=x) 
  
string = wrapper.fill(text=value) 
  
print (string) 
