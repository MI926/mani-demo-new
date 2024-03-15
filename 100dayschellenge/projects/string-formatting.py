# Get user input and convert to integer
y = (input("enter the number :- "))
x = int(y)

# Convert integer to binary and get length
binary1 = bin(x)[2:]
width = len(binary1)

# Loop through numbers 1 to x
for i in range(1, x + 1):

    # Convert each number to hexadecimal, octal, binary and decimal
    hexadecimal = str(hex(i)[2:])
    octal = str(oct(i)[2:])
    binary = str(bin(i)[2:])
    decimal = str(i)

    # Print each base conversion right justified to width of binary
    print(hexadecimal.rjust(width), octal.rjust(width),
          binary.rjust(width), decimal.rjust(width))
