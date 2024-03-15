"""
__author__ = Mani Gupta
__email__ = mg99263645@gmail.com
__status__ = Development
__version__ = 1.0.0
Description: THE Program is to find the word in the string.


"""
# making function which take a and b as a input where a is string or a paragraph and b is word which we us to find the position of the word only for the fist occurence of the word in the string.
def wordfinf(a, b):
    #printing the 1st ocurrence  number of the word of the string which we want to find

    print(a.find(b))
mmetrical or Palindromex = input("enter the string:- ")
y = input("enter the word:- ")
wordfinf(x,y)

"""
Description : THE Program is to count the word in the string.

"""
# making function which takes two values a as a string or a paragraph and b as a word which we want to find how many times it is repeated in the paragraph. 
def wordcount(a, b):
    #printing the number of times the word is repeated in the string
    print(a.count(b))
m = input("enter the parragraph you want :- ")    
k = input("enter the word you want to find:- ")
wordcount(m,k)
