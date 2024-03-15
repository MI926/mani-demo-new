'''print("hello")
a = str(input("enter the number 1 :- ",))
b = str(input("enter the number 2 :- ",))
c = str(input("enter the number 3 :- ",))
d = str(input(j"enter the number 4 :- ",))
e = str(input("enter the number 5 :- ",))
print(a + b + c + d + e)
#module is the code which writen alredy adu cycle improment not invention. it install by :- pip install "name of module". there are some bultine modules.
#first programe date 20 feb 2024
print("hello word")
#please dont use file names of modules.
#pythone as a calculater.
print(5+6+7+8, 99/22)
#comments are the lines which ignore by interpiter.
#for multiline commentuse:-3times'
print("mani the seeker")
print("the dohol is vaging")
#if i want to remove the space or dono ko same line me lane keliye at the end of print statmentes add "end = """"
print("mani the seeker", end = "")
print("the dohol is vaging")
#for any specific caracter add anything between comma here its 4.
print("mani the seeker", end = "4")
print("the dohol is vaging")`
print("mani the seeker", "the dohol is vaging", end = "4")
#escape sequance characters any like \n for new line
print("mani the seeker \n the dohol is vaging")
#variable is like a continer ye sirf valu stor karta jisko age kisi bhe time use karsakte hai. just like we define x for anything. variable are of 3 type float ex 34.89  int eg 1 string eg anything but no mathematical expresion applicable.
 
a = input("enter the number:- ", )
b = input("do you want to enter new number ",)
print(int(a) + int(b))
#by default inpute is a string
a = input("enter the number:- ", )
b = input("do you want to enter new number ",)
# for integer use int() for float () for str()
#how mulltiplication work on string it's just write it x times
print(10 * (a+b))
#for real multiplication on inpute make inpute as int
print(10 * int((a+b)))
print(10 * int((int(a)+int(b))))

#string slicing
c = "manithe"
#how to write mullti line string
d = """mani
       seeker
       the dohol is vaging"""
#for blank line before print use:- print("\n anything")
print("\nCreating a multiline String: ") 
#In this example, we will define a string in Python and access its characters using positive and negative indexing. The 0th element will be the first character of the string whereas the -1th element is the last character of the string.
print(c[0])
#print(c[0]) mean print the first character of string 0 starting point on pythone
print(c[1:3])
#print(c[1:3]) mean print the character from 1 to 2 because the last number is is always n-1 in python
print(c[1:])
#print(c[1:]) mean print the character from 1 to end
print(c[:3])
#print(c[:3]) mean print the character from 0(least) to 2
print(c[:-3])
#print(c[-1:3]) mean print the character from 0 to -3 (total length - given value) which actully 0 to 5 mean mani
print(c[-3:])
#print(c[-3:]) mean print the character from -3(means from 5) to end
print(c[-4:-3])
#print(c[-4:-3]) mean print the character from -4(from 3) to -3(to 4)
#In this example, we will reverse a string by accessing the index. We did not specify the first two parts of the slice indicating that we are considering the whole string, from the start index to the last index.
#Program to reverse a string 
gfg = "geeksforgeeks"
print(gfg[::-1])
#string slicing
list1 = list(String1) 
list1[2] = 'p'
String2 = ''.join(list1) 
print("\nUpdating character at 2nd Index: ") 
print(String2) 
  
#Updating Entire String if we just give two value for same variable then it only take last one value.
#Deleting a character
# Python Program to delete 
# character of a String 

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

print("Deleting character at 2nd Index:") 
del String1[2] 
print(String1)
#Deleting Entire String
# Python Program to Delete 
# entire String 

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

# Deleting a String 
# with the use of del 
del String1 
print("\nDeleting entire String: ") 
print(String1) 
#Escape Sequencing in Python
#While printing Strings with single and double quotes in it causes SyntaxError because String already contains Single and Double Quotes and hence cannot be printed with the use of either of these. Hence, to print such a String either Triple Quotes are used or Escape sequences are used to print Strings. 

#Escape sequences start with a backslash and can be interpreted differently. If single quotes are used to represent a string, then all the single quotes present in the string must be escaped and the same is done for Double Quotes. 


#strings are immutable. no changes are done after creating string but may be moddified at calling the string.
d = "Mani the seeker"
# Program to reverse a string 

gfg = "geeksforgeeks"

# Reverse the string using reversed and join function 
gfg = "".join(reversed(gfg)) 

print(gfg) 
# Printing Paths with the 
# use of Tab 
String1 = "Hi\tGeeks"
print("\nTab: ") 
print(String1) 
# Printing Paths with the 
# use of New Line 
String1 = "Python\nGeeks"
print("\nNew Line: ") 
print(String1) 
print(d.upper())
#print(d.upper()) mean print the string in upper case but it not change the original string
print(d.lower())
#print(d.lower()) mean print the string in lower case but it not change the original string
print(d.capitalize())
#print(d.capitalize()) mean print the string with first letter capitalized and all other are small
print(d.title())
#print(d.title()) mean print the string with first letter capitalized and all other are small
print(d.swapcase())
#print(d.swapcase()) mean print the string with upper case letter replaced by lower case and vice versa
print(d.isupper())
#print(d.isupper()) mean print true if all the letters are in upper case else false
print(d.islower())
#print(d.islower()) mean print true if all the letters are in lower case else false
print(d.center(20))
#print(d.center(20)) mean print the string with 20 spaces on left and right side of string
print(d.rstrip("r"))
#print(d.rstrip("r")) mean print the string from right side till the last r only aplicable for lasst letter.
print(d.lstrip("m"))
#print(d.lstrip("m")) mean print the string from left side till the first m only aplicable for first letter.
print(d.replace("mani", "the"))
#print(d.replace("mani", "the")) mean print the string with mani replaced by the
print(d.split(" "))
#print(d.split(" ")) mean split the string with space as a delimeter
print(d.split(" ", 1))
#print(d.split(" ", 1)) mean split the string with space (only for first space tak and the seeker is a string) as a delimeter
print(d.split(" ", 2))
#print(d.split(" ", 2)) mean split the string with space (only for first two space tak and mani, the, and seeker is a string
print(d.count("i"))
#print(d.count("i")) mean count the number of i in the string finds first occurance if i is not then give -1
print(d.count("i", 1, 5))
#print(d.count("i", 1, 5)) mean count the number of i in the string from 1 to 5
print(d.find("i"))
#print(d.find("i")) mean find the index of i in the string
print(d.find("i", 1, 5))
#print(d.find("i", 1, 5)) mean find the index of i in the string from 1 to 5
print(d.endswith("er"))
#print(d.endswith("er")) mean check the string ends with er or not
print(d.startswith("the"))
#print(d.startswith("the")) mean check the string starts with the or not
print(d.endswith("er", 1, 5))
#print(d.endswith("er", 1, 5)) mean check the string ends with er or not from 1 to 5
print(d.startswith("the", 1, 5))
#print(d.startswith("the", 1, 5)) mean check the string starts with the or not from 1 to 5
print(d.index("i"))
#print(d.index("k")) mean find the index of i in the string if not found then give error
#print(d.index("k", 1, 5))
#print(d.index("k", 1, 5)) mean find the index of k in the string from 1 to 5
print(d.isalnum())
#print(d.isalnum()) mean check the string is alphanumeric or not if anyone of the character is not alphanumeric then give false
print(d.isalpha())
#print(d.isalpha()) mean check the string is alphabet or not if anyone of the character is not alphabet then give false
print(d.isdigit())
#print(d.isdigit()) mean check the string is digit or not if anyone of the character is not digit then give false
print(d.isprintable())
#print(d.isprintable()) mean check the string is printable or not if anyone of the character is not printable then give false
print(d.isspace())
#print(d.isspace()) mean check the string is space or not if anyone of the character is not space then give false
print(d.istitle())
#print(d.istitle()) mean check the string is title or not if anyone of the character is not title then give false
print(d.title())
#print(d.title()) mean capitalize the first letter of each word in the string 
print(d.strip())
#print(d.strip()) mean remove the spaces from both side of the string
print(d.lstrip())
#print(d.lstrip()) mean remove the spaces from left side of the string
print( "_".join(d))
#print( "_".join(d)) mean add underscore between each word in the string in list all  are tree
#Formatting of Strings
#Strings in Python can be formatted with the use of format() method which is a very versatile and powerful tool for formatting Strings. Format method in String contains curly braces {} as placeholders which can hold arguments according to position or keyword to specify the order.
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
print(String1) 
#Integers such as Binary, hexadecimal, etc., and floats can be rounded or displayed in the exponent form with the use of format specifiers. 
# Formatting of Integers 
String1 = "{0:b}".format(16) 
print("\nBinary representation of 16 is ") 
print(String1) 

# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print("\nExponent representation of 165.6458 is ") 
print(String1) 

# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print("\none-sixth is : ") 
print(String1) 
#A string can be left, right, or center aligned with the use of format specifiers, separated by a colon(:). The (<) indicates that the string should be aligned to the left, (>) indicates that the string should be aligned to the right and (^) indicates that the string should be aligned to the center. We can also specify the length in which it should be aligned. For example, (<10) means that the string should be aligned to the left within a field of width of 10 characters.
# String alignment 
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks', 
										'for', 
										'Geeks') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1) 

# To demonstrate aligning of spaces 
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 
													2009) 
print(String1) 
#Left, center and right alignment with Formatting: 
#|Geeks     |   for    |     Geeks|
# GeeksforGeeks   was founded in 2009 !
#Old-style formatting was done without the use of the format method by using the % operator 
# Python Program for 
# Old Style Formatting 
# of Integers 

Integer1 = 12.3456789
print("Formatting in 3.2f format: ") 
print('The value of Integer1 is %3.2f' % Integer1) 
print("\nFormatting in 3.4f format: ") 
print('The value of Integer1 is %3.4f' % Integer1) 


#conditionals operator > , < , >=, <=, ==,!=
#!= is not equal to
#== is equal to
#< is less than
# > is greater than

e = int(input("enter the age number:- "))
if e >= 18:
    print("you are eligible to drive vhecal")
else:
    print("you are not eligible to drive vhecal")
if(e >= 18):
    print("you are eligible to drive vhecal")
else:
    print("you are not eligible to drive vhecal")
#elif means if the previous condition is false then check this condition and use for mulltiple condition.
if(e >= 18):
    print("you are eligible to drive vhecal")
elif(e >= 16):
    print("you are eligible to apply for learning permit")
else:
    print("you are not eligible to drive vhecal")
#elif is used for multiple condition.
# Nested if-else is used when you want to check multiple conditions and execute different code blocks based on each condition.

# Here is an example of nested if-else:

num = 15

if num > 10:
  print("Num is greater than 10")
  
  if num > 20:
    print("Num is also greater than 20")
  else:
    print("Num is not greater than 20")
  
else:
  print("Num is less than 10")
# match case statements in python
# match is a new keyword in Python 3.10
# match case statements allow you to check a value against several cases efficiently. 
# It is like a switch statement in other languages.

# Basic syntax:

match expression:
  case value1:
    #code to execute if expression matches value1
    ...
  case value2:
    #code to execute if expression matches value2 
    ...
  case _: 
    #code to execute if no case matches

# The expression is checked against the values for each case, and the code for the 
# first matching case is executed. The _ case acts like default in a switch statement.

# Some examples:

num = int(input("enter the number:- "))

match num:
  case 1:
    print("Number is 1")
  case 5:
    print("Number is 5")
  case 10:
    print("Number is 10")
  case _:
    print("Number is not 1, 5 or 10")
    
day = str(input("enter the day:- "))       

match day:
  case "Monday":
    print("Today is Monday")
  case "Tuesday":
    print("Today is Tuesday")
  case "Wednesday": 
    print("Today is Wednesday")
  case _:
    print("Today is some other day")
  

# match case is a cleaner way to check multiple conditions compared to long if/else chains.
#only one case matches the expression.
match num:
  case 1:
    print("Number is 1")
  case _ if  num!=5:
    print("Number is not 5")
  case _ if num!=8:
    print("Number is not 8")
#if statmennt satisfied the multiple condition then only first condition execute.
#for loop can iterate through a sequence of iterable objects such as lists, tuples, strings, and dictionaries.
num = int(input("enter the number:- "))

# Loop through numbers from 0 to num 
for i in range(0,num+1):
  
  # Print current number
  print(i)  
  
  # Skip printing 0
  if i == 0:
    continue
    
  # Increment i for next iteration
  i = i + 1
for k in range (0,num+1, 3):
  print(k)
# While loop means to execute a set of statements as long as a condition is true. Deffrence between while loop and for loop is that while loop executes a set of statements as long as a condition is true and for loop executes a set of statements a fixed number of times.
# While loop executes a set of statements as long as a condition is true.
# When to use while loop?
# which is faster while loop or for loop and when?
# while loop is faster than for loop when the number of iterations is known.
n = int(input("enter the number:- "))
i = 0
while i < n + 1:
    print(i)
    i = i + 1
else:
    print("i is no longer less than n")
    print("i is now", i)
    print("we are in the else block")
#else block is executed when the loop terminates normally.
#break and continue statements can alter the normal flow of a loop.
#break statement terminates the loop and transfers execution to the statement immediately following the loop.
#continue skip the curent block and goes back to the top of the next iteration.
#Do while loop is similar to while loop but the loop runes at least once regadless of the condition.
# I want to check whether the x > i + 1
x = int(input("enter the number:- "))
while True:
    print(x)
    i = 0
    if x > i + 1:
      break
    i = i + 1
#What is function?
#A function is a block of code which only runs when it is called.
#Functions help break our program into smaller and modular chunks.
#why we use functions?
#Functions help us to reuse code. and we dont have the longe code when ever we need to use it we just call thae functione .
def addtwonumber(a, b):
  add = a + b
  print(add)

a = int(input("enter the number:- "))
b = int(input("enter the number:- "))
addtwonumber(a,b)
#what is pass in function?
#pass mean run the code without giving an error where we just define the function but not write the code inside it.
#pass is used when we want to write the code later.
#def multiply(a, b):
  # now it gives an error 
def multiply(a, b):
  pass1v    b
# now no error
# the belo is the part of string
# Printing hello in octal 
String1 = "112\165\154\154\167"
print("\nPrinting in Octal with the use of Escape Sequences: ") 
print(String1) 
#by using / we say in octal or HEX-like things letters and numbers.
#if we have to use  

# Using raw String to       
# ignore Escape Sequences 
String1 = r"This is \110\145\154\154\157"
print("\nPrinting Raw String in Octal Format: ") 
print(String1) 

# Printing Geeks in HEX 
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ") 
print(String1) 

# Using raw String to 
# ignore Escape Sequences 
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ") 
print(String1) 
# Printing Geeks in Binary 

'''
#list is a collection of items in a particular order.
#list is a mutable datatype.
#list is a sequence of items.
x = int(input("enter the number:- "))
list = ["apple", "banana", "cherry"]
print(list[x])

#WHAT IS mean of mutable and immutable?
#mutable means it can be changed.

#it may consiste of different data types.
list1 = ["apple", "banana", "cherry", 1, 5.5, 7, True]
x1 = int(input("enter the number:- "))
print(list1[x1])
#to find if element is present in list we use in operator.
if "apple" in list1:
    print("Yes, 'apple' is in the fruits list")
#to find if element is not present in list we use not in operator.
if "mango" not in list1:
    print("No, 'mango' is not in the fruits list")
#must be of same data type for example belove if we "7" insted of 7 it will give not in list1.
if "7" in list1:
    print("Yes, '7' is in the  list1")
else:
    print("No, '7' is not in the  list1")
#same thing also aplies for strings.
if "7" in "apple":
    print("Yes, '7' is in the  'apple'")
else:
    print("No, '7' is not in the  'apple'")
