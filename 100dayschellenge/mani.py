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
  pass
# now no error
# the belo is the part of string
def multiply(a = 5, b = 6):
    print(a + b)
    print(a , "a is")
    print(b , "b is")
c = int(input("Enter thr number"))
multiply(a = c)
#we just take defult value of the b and a assign the value of c
# defult case me 1st value is for a and second value is for b 
#but we may define 1st value as b and second vslue as a
#ex
multiply(b = 15, a = 6)
#what is required array in function?
#in abve both are not required arrgument
def mulll(a, b = 8):
    print(a * b)
x = int(input("enter the number:- "))
mulll(b = x)
#above case give error as a is not given and it is required
#defult arrgument must be at last of the non define argument 

#variable length argument in function

#variable as tupule
def mulltiply(*args):
    b = 0
    for x in args:
        if b  == 0 :
          b = x
        else:
           
         b = b * x
    print(b)
    return b
c = 0
while True:
   x = int(input("enter the number:- "))
   if x == 1:
      multiply(x)
      break
   if c == 0:
      c = x
      continue
   
   mulltiply(x, c)
   c = mulltiply(x, c)


#list for mulltiple element
#list is a collection which is ordered and changeable. Allows duplicate members.
#the each element or item of a list is identified by an index. same as string
l = [1,2,3,4,5,6,7,8,9]
print(l)
print(l[0])
#adding element on lost.
#list may contain different data types.
l.append(13)
print(l)
# For finding an element in list must use same data type if we take number as string in if statement then it give error because the l contine integer


#jump index
#if we want to jump from a to c and skip b
print(l[0:3:2])
#so it 1st evalute 0 to 3 and then skip every second element from the privious one.
#list comprehension
#sort in list.  accending order 
l.sort()
print(l)
#and in decending order
l.sort(reverse = True)
print(l)
#reverse in the list.
l = [1,2,3,4,5,6,7,8,9]
l.reverse()
print(l) 
#for finding index of the element in list fist occurance.
print(l.index(5))
#for finding how many times comes an element in list.
print(l.count(5))
#why to use copy mot this n = l
#because then if we change the l then n will automatically changes
n = l
#inserting element at particular place(index)
l.insert(2, 26)
print(l, "is the value of l")
print(n, "is the value of n")
#if we use copy then it will not change the n
l = [1,2,3,4,5,6,7,8,9]
n = l.copy()
l.append(45)
#extend mean add at the last
l.extend([10,11,12])
print(l, "is the value of l")
print(n, "is the value of n")
#what is different between append and extend
#append treat the whole list as one element if we append x in l then whole element of x are treted as an single elment list in list

x = [1, 44, 12]
l.append(x)
print(l)
#what is tupple.
#it's the like list but not changeable
l = (1, 2, 3, 4)
print(l)
#l.append(12)
#it give error as tupple is not changeable
#if we want to change the tupple then we have to create new tupple
#l = (1)
print(type(l))
#in above it say the type is int not tuple so for tuple must use one comma after the num
#l = (1,)
print(type(l))
#now the type is tuple
#all indexing and other thing are same in tuple like list
#slcing of the tuple is possible 
print(l[1:])
#tuple also contain diffrent types like int, string, float etc.
#tupple is faster than list
#the below is the way to change tupule
#st -1 make an temporary list
#st -2 make changes in it
#st -3 convet it into tuple and must give same variable as previous tuple
l = (1, 5, 7, 6, 12)
print(l)
x = list(l)
x[1] = 10
x.extend((16, 18, 3, 13))
l = tuple(x)
print(l)
#tuple methods are same as the list
#What is the docstring?
#it may take as outpute. for write the def of the funtion
#it is just beloe the funtion.
def mul(a, b):
    # (3 commas) this just an example of docstring and just use in funtion to give it's defination
#    here thew first number is mulltiply by other (3 comass)
#    pass
a = 55
b = 77
mul(a, b)
print(mul.__doc__)
#above is just print the docstring of the function
#the possition is very important
#what is pep
#what is recurtion


def factorial(a):
    if (a == 0 or a == 1):
        return a
    else:
        return a * factorial(a-1)
a = int(input("enterthe number "))
print(factorial(a))
#must used the return don't print
#set its just don't store the repeted value and it is always give unorder iteam
#its unreplaceabl
#it may contain diffrent data type
#it cant be exces by index number
empty_set = set()  # Empty set is not like {} as it gives a dictionary
print(type(empty_set))
#if this {}
empty_set = {}
print(type(empty_set)) # this is give dictionary
empty_set = {"mani", "gupta", "gyan", "soham"}
#empty_set[1] = "mani" #it give error
#empty_set.append("mani") #it give error
# we may add element in the set.
empty_set.add("ifgxsfg")
print(empty_set)
#mathamatical oprations on set
s1 = {1, 2, 5}
s2 = {12, 5, 3, 2}
print(s1.difference(s2))
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.symmetric_difference(s2))
print(s1.issuperset(s2))
print(s2.issuperset(s1))
print(s1.issubset(s2))
print(s1.isdisjoint(s2))
# The update() method updates the set by adding elements from another set.

s1 = {1, 2, 5}
s2 = {12, 5, 3, 2}

s1.update(s2)
print(s1)  # {1, 2, 3, 5, 12}

# It can also add elements from other iterables like lists:

s1 = {1, 2, 5}
s2 = [3, 4, 6]

s1.update(s2)
print(s1)  # {1, 2, 3, 4, 5, 6}
s1.intersection_update(s2)
print(s1)
print(s2)
#above s1 update by intersection of s1 and s2
#remove an item using remove() function
s1.remove(3)
print(s1)
#diffrencs between remove and discard 
#remove raise error if element not present in set and discard dont raise error

s1.discard("mani")
print(s1)
#what is pop
#pop is used to remove the last element of the set but it is random
s2 = {1, 2, 5, 3, 12, 123}
b = s2.pop()
print(b)
#what is del
#del s1
#print(s1) #give an error of s1 not exist
#clear just remove all elemnt in the set
s1.clear()
print(s1)
#if value exist all are same as the list
#What is a dictionary? this is orderd
s = {
    1: "mani",
    2: "kumar",
    3: "suresh",
    4: "rohan",
    5: "raj",
    6: "ram",
    7: "shyam",
    8: "mohan"
}
print(s[2])
print(s)
#there are two way to exise dictionary
#by s[anything] s.get(anything)
print(s.get(9))# give none
#print(s[9])#this give error that 9 doesnt exist
#for printing all key
print(s.keys())
#for all key
print(s.values())
#for all values



for i in s.keys(): #to exces key
  print(s[i]) #to exces the value
  print(i)#to excess the key
  print(f"the value is {s[i]} and the key is {i}")
from hashlib import sha384


s1 = {1: "mani", 2: "rohan", 3: "krisna", 4: "raj", 5: "ram", 6: "shyam"}
s3 = {7: "mohan", 8: "sohan", 9: "roshan", 10: "suresh"}
print(s1)
print(s3)
s1.update(s3)
print(s1, "its after update") #updates the s1 and add all elemant of s3 to s1
s3.clear() #clear the all element of the discnary and make it empty discnary
print(s3)
#pop
s1.pop(1)
print(s1)#remove the value of 1  from s1 coresponding to key 1
s1.popitem()#remove the last value pair here its 10 : suresh

print(s1)
#del s1 delet whole discnary
del s1[3] #remove the value pair corresponding to key 3
print(s1)
#must know that data type is important on calling an element from list
#here we call a string so it gives error because the element is not there   
#how to ue else with for loop
for i in s1:
    print(i)
else:
    print(5)   
#it just exicute after for loop but if we break the for loop then else not  also same with while loop
for i in s1:
  if i == 4:
    break
  print(i)
else:
  print(35)    
#erore handling
#it important because if error accure the projgram not run after the error but if want that the program run even after the error
a = input("entere the number ")
# for i in range(1, 11):
#  print(f"{a} x {i} = {int(a)*i}")
# if enter an string in a then it just give error of invalid literal and program stops
# print("some important code id here")
# the above code dont run after the error
# to run the code after error we must have to use error handling
try:
    for i in range(1, 11):
        print(f"{a} x {i} = {int(a)*i}")
except Exception as e:  # we also use except:
    # print("error occure")
    print(e)
print("it is important code")
# now there is no error
# try meabs try to run if it dont give errorso run it without any hessitstion
# if erroe occour then run the code of exception and stor the erroe in e and print e
# dont block programe to run futher
# there are multiple type of error in python
#for handling spacific type of error
try:
    for i in range(1, 11):
        print(f"{a} x {i} = {int(a)*i}")
except SyntaxError:
    print("Sy")
except TypeError:
    print("type error")
except ValueError:
    print("Could not convert data to an integer.")
#what is final
#it must run irespective of the erroe is occure or not
#it always excicuted
#how it's special the iska kam to try except se bhi ho raha hai
#it mostly use in funtion where we retun some thing or break the loop etc.
#the code under the finaly must be exicuted
def mull(a, b):
    try:
        return a * b
    except Exception as e:
      print(e)
      return e
    print("mani gupta is the king")

print(mull(14, 15))
#above the mani gupta is the king not excicuted
#if we want to excute the print statemnet under the finaly then we must use finally
def mull(a, b):
    try:
        return a * b
    except Exception as e:
        print(e)
        return e
    finally:
        print("mani gupta is the king")
print(mull(16, 29))
#here the above code give mani gupta is the 
#how to rase the error in the programe
a = input("enter the number between 5 to 9")
if isinstance(a, int):
    if int(a)<5 or int(a)>5:
        raise ValueError("the number is not in between 5 to 9")
if a == "quit":
  pass
else:
  raise ValueError("the number is not entered")

#there is many ways to raise error in many diffrent cases
#JUSWTTEST FOR GIT AGAIN
#short hand if else
a = int(input("enter the num one"))
b = int(input("enter the num two"))
print(a) if a > b else print(b)
#at last must write else if not then it will give error and not excicuted
print(a) if a > b else print(b) if b == a else ""
#may use like that
c = 9 if a>b else 0 # give zero if a<b or a == b. and give 9 if a>b
print(c)
#what is the enumerate
#enumerate is just remove the use of index and use the value of the element 
a = [1, 12, 15, 4, 5, 6]
for index, i in enumerate(a):#here index give the value of how mnany times this loop runes before elemnt i index must be before i 
    print(index, i)
#index ki value defult zero se suru hoga but if i want to strt it from any specific value then.
for index, i in enumerate(a, start=1):
    print(index, i)
#how to make virtual envirment
#ye sirf ek alag envirment bana deta hai jiska main python se koi lenea dena nbahi hai
#its just make seprate envirement jiskop koi main python ke module install karna padta hai
# run this comand in the folder where you want to make virtual enverment:    python -m venv name
#to activate the virtual envirment         source venv/bin/activate
 #then just run regular commands to install modules/packages 
 #after that if you want to stop the virtual env run deactivatr
#there is file called requirment.txt its the list of packages whih used in that VE
#if some one wantr to copy whlo project of virtual env then this file help to install that same packages
# for making use the comand pip freeze > requirements.txt
#for them they just run    pip install -r requirements.txt

#import actually mean
#just it just like you use the whole code without writing it
import math
#we juste use all funtions of maths by math.funtion()
import math as m
#we use math as alike m.funtion()
from math import pi
#now we just copy the whole code of pi funtion from math
#so we use it like a defult funtion
print(pi)
from math import*
print(pi)
#now it just copy the whole code all funtion so we use it funtions defult way
#but dont use import* every time if module is big then it may cause trubool
#kisi MODULE kE KON KONSE funtions hai pata karne ke liye use dir
print(dir(math))
print(math.nan, type(math.nan))
print(isqrt(25))
#abve are the examples of hoe to use the funtions
# what is if __name__ == "__main__"
#it just used to check the name of the file is main or not
#it prevent the file from running if it is not main
#it is used to make the file as a module
#jab ham kisi module ko import karte hai to module ke sare funtions run hote hai hai.
#but hame to khali funtions ko tab run kaerna hai jab ham use call kare so it just stop funtion to run
# example let creat module name mani.py
import manie
a = "mani gupta king"
manie.name1() #see here mani gupta is printing 2 times for that we use if __name__ == "__main__"
#so now we update the code of manie
#now it just print onces
#ye batata hai ki isko kaha se call kar rahe hai same file se ya kisi aur file se as module leke
#here it is not give main it gives manie
# what is os module
#it just use to use some functions of copy file pastcut edit, delet, creater, rename etc
import os
if (not os.path.exists("osmodule test")):
  os.mkdir("osmodule test")
for i in range(0, 50):
  os.mkdir(f"osmodule test/folder{i + 1}")
 #os.mkdir use for making folder and the name is inside os.module("name")
 #os.rename use for renaming the folder
#for i in range(0, 50): #thsi use to make the files with name folder1, folder2, folder3, folder4, folder5....etc
for i in range(0, 50):
  os.rename((f"osmodule test/folder{i + 1}"), (f"osmodule test/folder{i + 1}.py"))
#os.remove use for deleting the folder
#for i in range(0, 50):
  #os.remove(f"osmodule test/folder{i + 1}.py")
#os.rmdir use for deleting the folder
#what is diffrent between the rmdir and remove
#the main difference is that os.remove() is used to delete files, while os.rmdir() is used to remove empty directories.

for i in range(0, 50):
  os.rmdir(f"osmodule test/folder{i + 1}.py")
#os.chdir use for changing the directory
os.chdir("osmodule test")
#os.getcwd use for getting the current directory
print(os.getcwd())
#os.listdir use for getting the list of files in the directory
print(os.listdir())
#os.path.exists use for checking the file or folder is exists or not
print(os.path.exists("osmodule test"))
#os.path.isfile use for checking the file is file or not
print(os.path.isfile("osmodule test"))
#os.path.isdir use for checking the file is folder or not
print(os.path.isdir("osmodule test"))
#os.path.join use for joining the path
print(os.path.join("osmodule test", "folder1"))
#os.path.basename use for getting the name of the file
print(os.path.basename("osmodule test/folder1"))
#os.path.dirname use for getting the name of the folder
print(os.path.dirname("osmodule test/folder1"))
#os.path.getsize use for getting the size of the file
print(os.path.getsize("osmodule test/folder1.py"))
#global vs local
a = 5
def funtion():
  a = 10 
  print(a)#it prints local a a = 10
  #so 
  
print(a)#it prints global a a = 5
print(funtion())#it prints local a a = 10
#for changing global a in funtion we use global
def funtion():
  global a
  a = 10
  print(a)
print(funtion())#changing the global a in funtion
#file handling
#open use for opening the file
#w use for writing the file
#r use for reading the file
#a use for appending the file
#x use for creating the file
#b use for opening the file in binary mode
#whatever is used in open function is used for opening the file
a = open('100dayschellenge/projects/filehandling/file.txt', 'r', encoding='utf-8')
print(a)
text = a.read()
print(text)
a.close()
#the above shows how to use the open function read mode and execess the file's data
#the above code is used for reading the file
#a.close() use for closing the file
#the above code is used for closing the file
#now we use write mode
#a = open('100dayschellenge/projects/file.txt', 'w')
#a.write("hello")

#the above code is used for writing the file
#we remove the prebiouse text and write the new text here it's hello
a = open('100dayschellenge/projects/filehandling/file.txt', 'a')
a.write("hello\n")
a.close()#close is must
#if we use write and file is not exist it will creat file with that name
#append also able to write the file and craet new file it not exist
a = open('100dayschellenge/projects/filehandling/file1.txt', 'w')#here file1.txt not exist but i creat new file and add hello
a.write("hello\n")
a.close()
#the above code is used for creating the file
#the new way to doing same thing is by with
with open('100dayschellenge/projects/filehandling/file2.txt', 'w') as file:
  file.write("hello hiie\n")
with open('100dayschellenge/projects/filehandling/file2.txt', 'r') as file:
  print(file.read())
#the above code is used for reading the file
with open('100dayschellenge/projects/filehandling/file2.txt', 'a') as file:
  file.write("hello hiie\n")
#how to use line by line
with open('100dayschellenge/projects/filehandling/file2.txt', 'r') as file:
  for line in file:
    print(line)
  else:
    print("it's not line")
#the above code is used for reading the file line by line
#the else is used for checking the end of the file
with open('100dayschellenge/projects/filehandling/MAKSEXAMPLE.TXT', 'r') as file:
  for line in file:
    print(line)
    b = line.split(", ")
    #print(line.split())
    print(f"in physics out of 100 students gets {b[0]}")
    print(f"in maths out of 100 students gets {b[1]}")
    print(f"in chemistry out of 100 students gets {b[2]}")
    
  
  else:
    print("it's not line")
  #the above code is used for reading the file line by line and spliting the data



from concurrent.futures import thread


with open('100dayschellenge/projects/filehandling/MAKSEXAMPLE2.TXT', 'w') as file1:
  with open('100dayschellenge/projects/filehandling/MAKSEXAMPLE.TXT', 'r') as file2:
    for line in file2:
      b = line.split(", ")
      file1.write(f"in physics out of 100 students gets {b[0]}\n")
      file1.write(f"in maths out of 100 students gets {b[1]}\n") 
      file1.write(f"in chemistry out of 100 students gets {b[2]}\n")
    else:
      print("it's not line")
#the above code is used for reading the file line by line and spliting the data and writing the data in new file`
# what is seek in file handling in the python
# this just redifine the current ppositon in the file agar seek(10)`then countinbg start from 10
with open('100dayschellenge/projects/filehandling/MAKSEXAMPLE2.TXT', 'r') as file1:
  file1.seek(10)
  print(file1.read())
  #the above code is used for reading file but start from 10th charecter of the file
#the above code is used for reading file but start from 10th charecter of the file
with open('100dayschellenge/projects/filehandling/MAKSEXAMPLE2.TXT', 'r') as file1:
  file1.seek(10)
  print(file1.read(20))
  #the above code is used for reading file but start from 10th charecter of the file and read 20 charecter
#what is trucute in file handling in the python
#this is used for trucating the file
with open('100dayschellenge/projects/filehandling/MAKSEXAMPLE2.TXT', 'r+') as file1:
  #file1.truncate(10)
  print(file1.read())
  #the above code is used for reading file and removing other charecter. only containig 10 charecter in file
#what is tell in file handling in the python
#this is used for telling the current position in the file
with open('100dayschellenge/projects/filehandling/MAKSEXAMPLE2.TXT', 'r+') as file1:
  file1.seek(10)
  print(file1.tell())
  #the above code is used for reading file and tell the current position in the file
#what is mode in file handling in the python
#this is used for telling the mode in which file is open
with open('100dayschellenge/projects/filehandling/MAKSEXAMPLE2.TXT', 'r+') as file1:
  print(file1.mode)
  #the above code is used for reading file and tell the mode in which file is open
#the mode is r+ is used for reading and writing
#what is buffering in file handling in the python
#this is used for telling the buffering in which file is open
with open('100dayschellenge/projects/filehandling/MAKSEXAMPLE2.TXT', 'r+') as file1:
  print(file1.buffer)
  #the above code is used for reading file and tell the buffering in which file is open
#what is the lamda function
#lamda function is used for creating function in one line
squere = lambda x: x*x
print(squere(2))
#the above code is used for creating function in one line
factorial = lambda x: 1 if x == 0 else x * factorial(x-1)
print(factorial(5))
three = lambda x,y,z: (x+y+z)/5
print(three(10,20,30))
n_num_avg = lambda *x: sum(x)/len(x)
print(n_num_avg(10,20,30,40,50))
#we may pass function as a parameter to another function
def add(fx, y):
  return fx(y) + 8
print(add(factorial, 5))
#the above code is used for passing function as a parameter to another function and adding 8 to it
#what is map fillter and reduce function
#map function is used for applying function to all the element of the list

my_list = [1,2,3,4,5]
print(list(map(squere, my_list)))
#basicaly it take each valueof list and pass it in the funtion and then append it to new list at the end give new list
#the above code is used for applying function to all the element of the list
#reduce function is used for applying function to all the element of the list
from functools import reduce
print(reduce(lambda x, y: x + y, [1,2,3,4,5]))
#the above code is used for applying function to all the element of the list
#it take 2 1st two values and then pass to funtion the output is now the fist value and then 1st and second pass to funtion and so on
#at the end give the all values output
#what is fillter function
#fillter function is used for applying function to all the element of the list and then filter the value
#basicaly it take each valueof list and pass it in the funtion and then append it to new list at the end give new list
def my_func(x):
  return x%2 == 0
print(list(filter(my_func, my_list)))#it give the number which are even
#what is diffrent between is and == 
#both are compare the two objects
#== compare the value
# is campare the location in objects identity compare
a = 5
b = 5
print(a is b)
#if object is immutable then it will give true because python use same memeory and refure three from both side
#so it's value and location both are same
#if object is mutable then it will give false because python use different memeory and refure three from both side
#for example list
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)#false as two diffrent location used as it is immutable

print(a == b)#true as both values is same
#what is object orianted programing(oop)
#it just store the variable and able to give diffrent value
#like railway form wher the formate is fix everyone have diffrent details
#below we just add some deteils but we may change them for diffrent cases
class employ:
  name = "mani"
  occ = "SDE1"
  salary =  150000
#by a = employ() we says that all the funtions of the class employ are used by a
#by a.something we call the variables of the a
a = employ()
print(a.name, a.occ, a.salary)
class employ:
  name = "mani"
  occ = "SDE1"
  salary =  150000
  def info(self):
    print(f"This is {self.name} there salary is {self.salary} There role is {self.occ} ")
#above info is funtion which 
#it's just like sabki infoprmation ek formate me store kare sakte hai
#like a.employ() mean a ke information b.employ() is all information of b

a = employ()
print(a.info())
b = employ()
b.name = "mudit"
b.occ = "manager"
b.salary = "200000"
print(b.info())#self mean jiske liye ye call horaha hai
c = employ() 
print(c.info())
#the above is the sytntext to use
#if we don't use defule value then we need to use cons

class mani :
  name = " hsk"
  occ = "SDK@"
  salary = "28883"
  print(f"this is {name} there role is {occ} there pay is {salary}")
e = mani()
e.name = "kuntramal"
e.occ = "SDF"
e.salary = 3289649
#we have to use new funtion because it only runs one
#so we need function which run after editing value.
#that reson we define info

class Person:
  def __init__(self, n, o, s):
    print('hii')
    self.name = n
    self.occ = o
    self.salary = s
    #print(f"This is {self.name} there salary is {self.salary} There role is {self.occ} ")
  def info(self):
     print(f"This is {self.name} there salary is {self.salary} There role is {self.occ} ")
print(Person("mani", "SDE1", 50000))
a = Person("manij", "SDE1", 50000)
b = Person("gorakkh", "Maneger", 150000)
a.info()
b.info()
#so above we don't define amything with defult value so we used functions
#What is decoraters in python
#it's just decorate the funtion add somrthing at begening and at the end

def greeting(fx):
    def mfx():
        print("hii thanks for calling me")
        fx()
        print("thanks")
    return mfx


@greeting#its call by this
def hello():
  
  print("you are in hello")
hello()
greeting(hello())#this is also do same thing its like funtion in funtion

def greeting1(fx):
  def mxf(*args, **kwargs):
    print("this is first part")
    fx(*args, **kwargs)
    print("you are gong to deport") 
  return mxf
@greeting1
def add(a, b):
  print(a + b)


add(2, 23254)  
#what is geeter seeter and deleter

class MyClass:
  def __init__(self, value):
      self._value = value
      print("this is init")
    
  def show(self):
    print(f"Value is {self._value}")
    print("this is in show")
    
  @property
  def ten_value(self):
      print(f"THIS IS ten_value, {self._value}")
      return 10 * self._value
      
  @ten_value.setter
  def ten_value(self, new_value):
      self._value = new_value / 10
      print("ten_value1")

#obj = MyClass(10)
#obj.ten_value = 67
#print(obj.ten_value)
#obj._value = 8
#obj.show()
#like jaise ham kisi ko acces nahi dena chate hai direct so we use _varialbe;le
#for the seek of convinenes we judt use geeter and seeter to edite the value and set it
#seeter use to take value
#geeter used to change the value
#we may do this thing without geeter and set but it's good practice
 #Inheritage baap  beta. beta bana ne ko in heritage bolte hai.
 #whereson has all charecters of father and some new which is there own
class mani12(MyClass):
  def __init__(self, programing):
    self._programing = programing
  def show1(self):
    print(f"Value is programing is {self._programing}")

a = mani12("Python")
a.show1()
a.ten_value = 33
print(a.ten_value)
a.show()
b = mani12("C++")
b.show1()
b._value = 80
b.show()
#inheritage me direct variable ko call nahi kar sakte hai iskeliye alag alag hi call kaena padta hai
#in python there is no any thing called privet and protected bas itna hai ki __ variable name dene par
#isko pura naming convention badal jaiga ga like valur to a._class__value
#this is to excees private variable
class mani325():
  def __init__(self):
    self.__programing = "programing"
  def show1(self):
    print(f"Value is programing is {self.__programing}")
m = mani325()
#m.__programing = "C++"#it doesn't change programing
m._mani325__programing = "Python"#but it change it to Python
m.show1()
#static methods
#jinko self ki jarurat nahi padti jisko class ke bhar bhi use kar sakte hai
class static:
    @staticmethod
    def mull(a, b):
        print(a * b)

print(static.mull(15, 25))#by this way also accesable
a = static()#this is also valid way to exise 
a.mull(25, 45)


#instance vs class variable
class mania():
  
  def __init__(self, prog) :
     self.programe = prog
  def add(a, b):
    print(a + b)
c = mania("python")
#c.add(12, 18)# it give error TypeError: mania.__init__() missing 1 required positional argument: 'prog'
#why because this code is same as mania.add(c)
#so here clearly c is one variable and we also give two othere so this is the reson
#let if we just add three variable in funtion
class mania():
  
  def __init__(self, prog) :
     self.programe = prog
  def add(a, b, c):
    print(c + b)
    
c = mania("python")#above we just leave a as a take c
#we may define it as self so if we make changes in c then it may change by self
c.add(243, 3487)
#as we can't use anything from class so no need of self
#class vs instence variable
class mania():
  company = "apple"
  def __init__(self, prog) :
     self.programe = prog
  def add(a, b, c):
    print(c + b)
  def show(self):
    print(f"her her company is {self.company} and languge is {self.programe}")
a = mania("python")
a.company = "amazon"
a.show()
#we may define inside it it woks same in this case but if i want to know count of the
#data enter then its not usefull in instence
#it also helphfull when you want to a change whole variable at onc for all then this works leke mania.company = "anything"
class mania():
    employ = 0
    def __init__(self, prog):
        self.programe = prog
        mania.employ += 1 #this is the syntext
    def add(self, b, c):
        print(c + b)
    def show(self):
        print(f"her her company is {self.company} and languge is {self.programe} and number is {mania.employ}")

a = mania("python")
a.company = "amazon"
a.show()
b = mania("python")
b.company = "amazon"
b.show()
mania.employ = 0
#class method to change the company name by funtion for all the cases
class mania():
    company = "apple"
    def __init__(self, prog):
        self.programe = prog
    def add(self, b, c):
        print(c + b)
    def show(self):
        print(f"her her company is {self.company} and languge is {self.programe} and number is {mania.company}")
    @classmethod
    def changecompany(cls, new_company):
      cls.company = new_company
a = mania("python")
#a.company = "amazon"
a.show()
b = mania("python")
#b.company = "amazon"
b.show()
mania.changecompany("amazon")
b.show()
a.show()
#string slicing in class for make complex data simple
#like we have given name and all like mani-120000-SDE!
#then we can't able to use it directly and if we split it
#for every people then it mees the code
class mania():
    company = "apple"
    def __init__(self, prog, name, salary):
        self.programe = prog
        self.name = name
        self.salary = salary
    def add(self, b, c):
        print(c + b)
    def show(self):
        print(f"her her company is {self.company} and languge is {self.programe} and number is {mania.company} salary is {self.salary}, name is {self.name}")
    @classmethod
    def unformatetoform(cls, input_str):
        return cls(input_str.split("-")[0], input_str.split("-")[1], input_str.split("-")[2])
    @classmethod
    def changecompany(cls, new_company):
        cls.company = new_company
a = mania.unformatetoform("mani-120000-SDE")
a.show()
b = mania.unformatetoform("jani-120000-SDE")
b.show()
mania.changecompany("amazon")
b.show()
a.show()
#dir(), __dict__ and help() usage
print(dir(b))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
#it just print all methods of the class or funtion
print(dir(str))
print(b.__dict__)
#it just give al variable with there value from class
print(help(b))
#it give detail description of the class
#what is supeer method
class parenst():
  def __init__(self, name, salary):
    self.name = name
    self.sal = salary
  def show(self):
    print(f"name is {self.name} and salary is {self.sal}")
class son(parenst):
  def __init__(self, name, salary, lang, exp):
    super().__init__(name, salary)
    self.languge = lang
    self.exp = exp
  def show(self):
    print(f"name is {self.name} and salary is {self.sal} and experiance is {self.exp} and languge is {self.languge}")
m = son("mani", "100000", "python", "5 year")
m.show()
#the above code just helpfull for don't repeat the code every time
#what are the magic method
class parenst():
  def __init__(self, name, salary):
    self.name = name
    self.sal = salary
  
  def show(self):
    print(f"name is {self.name} and salary is {self.sal}")
    
  def __str__(self):
    return f"name is {self.name} and salary is {self.sal}"
    
  def __repr__(self):
    return f"parenst(name={self.name}, salary={self.sal})"
    
  def __len__(self):
    return len(self.name)
    
  def __add__(self, other):
    return self.name + other
    
  def __eq__(self, other):
    return self.name == other.name and self.sal == other.sal
    
  def __call__(self):
    print("hii call called")
a = parenst("mani", 100000)
print(a) #it just print the callable and run the funtion __str__
print(repr(a))#Provide string representations for objects
#__add__ method in Python defines how will be the objects of a class added together. It is also known as overloaded addition operator.

#Now add __add__ method to String class

print(a + "mani")#it just add something to value of predefine 
a()
print(a.name == "mani")  # campare the value of variable
# method overloading
# like using parents method with some extra modifications


class parenst:
    def __init__(self, name, salary):
        self.name = name
        self.sal = salary

    def show(self):
        print(f"name is {self.name} and salary is {self.sal}")
    def salal(self):
      return int(10000)
class son(parenst):
    def __init__(self, name, salary, lang, exp):
        super().__init__(name, salary)
        self.languge = lang
        self.exp = exp

    def show(self):
        print(f"name is {self.name} and salary is {self.sal} and experiance is {self.exp} and languge is {self.languge}")

    def salaryplus(self, add):
        return add + super().salal()

m = son("mani", "100000", "python", "5 year")
m.show()
print(m.salaryplus(10000))
#the above is used for addind or doing something extra with perents method
#opperator overloading
#__add__  __subreact__ etc
class parenst():
  def __init__(self, name, salary):
    self.name = name
    self.sal = salary
  
  def show(self):
    print(f"name is {self.name} and salary is {self.sal}")
    
  def __str__(self):
    return f"name is {self.name} and salary is {self.sal}"
    
  def __repr__(self):
    return f"parenst(name={self.name}, salary={self.sal})"
    
  def __len__(self):
    return len(self.name)  
  def __add__(self, other):
    return self.sal  + other
  def __sub__(self, other):
    return self.sal - other
  def __mul__(self, other):
    return self.sal * other
  def __truediv__(self, other):
    return self.sal / other
  
a = parenst("mani", 10000)
print(a - 100)
print(a + 1000)  
print(a * 2)
print(a / 10)
#multiple inheritage
class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show() 
print(DancerEmployee.mro())#this is used to decide priority order if funtion with same name present
#fist come fist serve
#multilevvel inheritAGE 
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o = Dog("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())

#mullti levell inheritage above
#Hybrid class
# Example of a hybrid class
class parent():
  pass
class ParentClass1(parent):
  pass
class ParentClass2(parent):
  pass

class HybridClass(ParentClass1, ParentClass2):
    def __init__(self):
        ParentClass1.__init__(self)
        ParentClass2.__init__(self)

    def hybrid_method(self):
        print("This is a hybrid method")
#above is example of hybrid class
#Higherical class
class ceo():
  pass
class man1(ceo):
  pass
class man2(ceo):
  pass
class man3(ceo):
  pass
class em1(man1):
  pass
class em2(man1):
  pass
class em3(man1):
  pass
class em4(man1):
  pass
class em5(man1):
  pass
class em1(man2):
  pass
#time modul
import time
def for01():
  for i in range(1, 1000):
    #print(i)
    continue
def while01():
  i = 0
  while i < 1000:
    #print(i)
    i = i + 1
seconds = time.time()
for01()
print(time.time() - seconds)
sec = time.time()
while01()
print(time.time() - sec)
#to find the time how much time an funtion take to perform task
import time
#sleep in time
print("zero second")
time.sleep(3)#it just wait for 3 sec befor excicuting below code
print("it's after 3 sec")
print(str(time.localtime()))
print(str(time.gmtime()))#it for UTC
t = (2024, 4, 27, 15, 20, 26, 4, 118, 0)

result = time.asctime(t)
print("Result:", result)#it's just like tuple number to year date and time etc
#In Python, the asctime() function takes struct_time as an argument and returns a string representing it.
#Similar to mktime(), the time_tuple has the following structure:

#(year, month, day, hour, minute, second, weekday, day of the year, daylight saving)

import argparse
parser = argparse.ArgumentParser(description ='Process some integers.')
parser.add_argument('integers', metavar ='N', 
					type = int, nargs ='+',
					help ='an integer for the accumulator')

parser.add_argument(dest ='accumulate', 
					action ='store_const',
					const = sum, 
					help ='sum the integers')

args = parser.parse_args()
print(args.accumulate(args.integers))
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.square**2)
