"""Removes duplicate substrings of length k from the input string.

Iterates through the input string, taking substrings of length k.
Adds unique substrings to a list. Concatenates the unique substrings
back into a string, omitting duplicates.
"""

# Get input string from user
a = input("enter the string")

# Get substring length k from user
b = int(input("enter the number of leeters you want to break"))
p = b

# Initialize variables
c = ""
n = 0
d = []

# Iterate through string, taking substrings of length k
for i in a:
    e = a[n:b]
    if len(e) < p:
        break
    d.append(e)
    b = b + 1
    n = n + 1

# Initialize list to hold unique substrings
g = []

# Print for debugging
print(p)
print(b)
print(d)

# Add unique substrings to list
for i in d:
    if i not in g:
        g.append(i)

# Concatenate unique substrings back into string
h = 0
l = len(g)
k = ""
m = 1

for i in g:
    h = 0
    m = m + 1
    o = l - m
    for j in i:
        if h == 0:
            k = k + j
            h = h + 1
        if o == -1:
            k = k + i[1:]
            print(i[1:])
            break

# Print result
print(k)

print(g)
