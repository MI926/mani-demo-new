import textwrap
y = (input("enter the number :- "))
x = int(y)
binary1 = bin(x)[2:]
width = len(binary1)

for i in range(1, x + 1):
    hexadecimal = str(hex(i)[2:])
    octal = str(oct(i)[2:])
    binary = str(bin(i)[2:])
    decimal = str(i)
    print(hexadecimal.rjust(width), octal.rjust(width), binary.rjust(width), decimal.rjust(width))
   
