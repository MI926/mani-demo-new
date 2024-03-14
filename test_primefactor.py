'''# Program to reverse a string 

gfg = "geeksforgeeks"

# Reverse the string using reversed and join function 
gfg = "".join(reversed(gfg)) 

print(gfg) 
# Escaping Single Quote 
String1 = 'I\'m a "Geek"'
#\ is not count for \ in in outpute use \\ one for skiping and one for print.

print("\nEscaping Single Quote: ") 
print(String1) 
# eg for the above.
# Printing Paths with the 
# use of Escape Sequences 
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ") 
print(String1) 
# Python Program for 
# Formatting of Strings 

# Default order 
String1 = "{} {} {}".format('Geeks', 'For', 'Life') 
print("Print String in default order: ") 
print(String1) 

# Positional Formatting 
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life') 
print("\nPrint String in Positional order: ") 
print(String1) 

# Keyword Formatting 
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life') 
print("\nPrint String in order of Keywords: ") 
# Python Program for 
# Old Style Formatting 
# of Integers 

Integer1 = 12.3456789
print("Formatting in 3.2f format: ") 
print('The value of Integer1 is %5f' % Integer1) 
print("\nFormatting in 3.4f format: ") 
print('The value of Integer1 is %3.4f' % Integer1) 
#The output of the boolean operations between the strings depends on the following things: 

#Python considers empty strings as having a boolean value of the ‘false’ and non-empty strings as having a boolean value of ‘true’.
#For the ‘and’ operator if the left value is true, then the right value is checked and returned. If the left value is false, then it is returned
#For the ‘or’ operator if the left value is true, then it is returned, otherwise, if the left value is false, then the right value is returned.
a = '' 
b = 'mani'

# repr is used to print the string along with the quotes 

# Returns a 
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

a = '' 

# Returns True 
print(repr(not a))
print("mani Gupta")
#it just print anything 

print(String1) 
'''
#In Python, a string of required formatting can be achieved by different methods. Some of them are; 1) Using % 2) Using {} 3) Using Template Strings In this article the formatting using % is discussed. The formatting using % is similar to that of ‘printf’ in C programming language. %d – integer %f – float %s – string %x – hexadecimal %o – octal The below example describes the use of formatting using % in Python. 
# Python program to demonstrate the use of formatting using % 

# Initialize variable as a string 
variable = 15
string = "Variable as string = %s" %(variable) 
print (string ) 

# Printing as raw data 

print ("Variable as raw data = %r" %(variable)) 

# Convert the variable to integer 
# And perform check other formatting options 

variable = int(variable) # Without this the below statement 
						# will give error. 
string = "Variable as integer = %d" %(variable) 
print (string) 
print ("Variable as float = %f" %(variable)) 

# printing as any string or char after a mark 

print ("Variable as printing with special char = %c" %(variable)) 

print ("Variable as hexadecimal = %x" %(variable)) 
print ("Variable as octal = %o" %(variable)) 
   
a = "M"
print("this is use of %%c = %c" %(a))
#it just use full for only one character>
#for multiple character use *

