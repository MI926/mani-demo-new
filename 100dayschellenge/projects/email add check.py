import re

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Za-z]\b'
#this is the way to defing the name@email.come
#[A-Za-z0-9._%+-] this is for name which contain a;; lettrrs for small to large and some special charecter
#@[A-Za-z0-9.-] this is for company which compes after @



# Define a function for
# for validating an Email
def check(email):

	# pass the regular expression
	# and the string into the fullmatch() method
	if(re.fullmatch(regex, email)):
		print("Valid Email")

	else:
		print("Invalid Email")

# Driver Code
while True:
    a = input("Enter the Email")
    if a == "":
        break
    check(a)
