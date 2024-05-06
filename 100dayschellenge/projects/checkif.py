# Python3 code to demonstrate working of 
# Check if string repeats itself 
# Using List comprehension + Brute Force 

# initializing string 
test_str = "abcabcbb"

# printing original string 
print("The original string is : " + test_str) 

# using List comprehension + Brute Force 
# Check if string repeats itself 
res = ""
for i in range(1, len(test_str)//2 + 1): 
	if (not len(test_str) % len(test_str[0:i]) and test_str[0:i] *
		(len(test_str)//len(test_str[0:i])) == test_str): 
		res = test_str[0:i]

# printing result 
print("The root substring of string : " + res)
