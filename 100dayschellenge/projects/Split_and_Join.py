
# Ask user to input a paragraph
x = str(input("enter the paragraph :- "))

# Split the paragraph into words using split() method
b = x.split(" ")
# Print the list of words  
print(b)  

# Join the words using '_'
c = "_".join(b)
# Print the joined string
print(c)

# Explanation:
# 1. Ask the user to input a paragraph and store it in variable x
# 2. Split the paragraph in x into a list of words using the split() method
#    and store the list in variable b
# 3. Print out the list of words b  
# 4. Join the list of words b into a string using '_' as the separator
#    and store the joined string in variable c
# 5. Print out the joined string c
