#Calculator
#day 1
print("1 for addition")
print("2 for Subraction")
print("3 for Multiply")
print("4 for division")
choice = input("Enter your choice(1/2/3/4): ")
if choice in ('1', '2', '3', '4'):
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    if choice == '1':
        print(number1, "+", number2, "=", (number1 + number2))
    elif choice == '2':
        print(number1, "-", number2, "=", (number1 - number2))
    elif choice == '3':
        print(number1, "*", number2, "=", (number1 * number2))
    elif choice == '4':
        print(number1, "/", number2, "=", (number1 / number2))
else:
         print("Entered input is invalid")
