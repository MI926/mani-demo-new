'''def stringfo(k, l, m):
    a = int(input("enter the number:- "))
    b = int(input("enter the number:- "))
    c = int(input("enter the number:- "))
    String1 = "{a} {b} {c}".format(k, l, m)
    print("Print String in default order: ")
    print(String1)


k = input("enter word:- ")
l = input("enter word:- ")
m = input("enter word:- ")
stringfo( k, l, m)
def stringfo(k, l, m):
    a = int(input("enter the number:- "))
    b = int(input("enter the number:- "))
    c = int(input("enter the number:- "))
   
    # zip together the numbers and words and sort
    words = sorted(zip([a, b, c], [k, l, m]))

    # join the sorted words together
    String1 = " ".join([w[1] for w in words])
    print("Print String in default order: ")
    print(String1)

k = input("enter word:- ")
l = input("enter word:- ")
m = input("enter word:- ")
stringfo( k, l, m)
'''
def stringfo(k, l, m):
    # Taking input for the positions
    a = int(input("Enter the position of '{}': ".format(k)))
    b = int(input("Enter the position of '{}': ".format(l)))
    c = int(input("Enter the position of '{}': ".format(m)))
    
    # Using the input positions to format the string
    # I dont know this syntax of python.
    # I just googled it.
    
    
    # Printing the formatted string
    print("Print String in user-defined order: ")
    print(String1.format(k, l, m))

# Taking inputs outside the function
k = input("Enter word for 'a': ")
l = input("Enter word for 'b': ")
m = input("Enter word for 'c': ")

# Calling the function with input values
stringfo(k, l, m)
