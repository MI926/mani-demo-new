


def changei(b, a):
    match a :
        case 'octal':
            converted = oct(b)
        case 'hex':
            converted = hex(b)
        case 'decimal':
            converted = str(b)  
        case 'float':
            converted = float(b)  
        case  'string':
            converted = str(b) 
        
        case 'binary':
            converted = bin(b)
        case _:
            print("Invalid input")
    
    print("Variable converted to {}: {}".format(a, converted))

# Taking user input for the number and conversion format
b = float(input("Enter the number: "))
conversion_format = input("Enter the conversion format (octal, hex, binary, decimal, float, string): ")

# Calling the function with user input values
changei(b, conversion_format)
