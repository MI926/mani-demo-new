def maniman(a, b):

    print(repr(a and b)) 

    # Returns a 
    print(repr(b and a)) 

    # Returns b	 
    print(repr(a or b)) 

    # Returns b 
    print(repr(b or a))	 

    a = 'for'

    # Returns b 
    print(repr(a and b)) 

    # Returns a 
    print(repr(b and a)) 

    # Returns a	 
    print(repr(a or b)) 

    # Returns b	 
    print(repr(b or a))	 

    a='the python king'

    # Returns False 
    print(repr(not a))		 
    
a = input("Enter the first number: ")
b = input("Enter the second number: ")
maniman(a, b)