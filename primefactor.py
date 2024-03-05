x = int(input("enter the number :- "))

"""Prints out all prime factors of a given integer.

Iterates through all numbers from 1 to the input number. Checks if the 
current number divides the input number without remainder, indicating it is
a factor. Further checks if the current factor is prime by trying to divide 
it by all numbers from 2 to itself. If no division is without remainder, 
the current factor is prime. 

The prime factors are printed as they are found. After printing a factor,
the input number is divided by that factor to reduce it for further 
factorization.

Args:
    x: The integer to find all prime factors of.
"""
for i in range(1,x+1): # start loop from 1 to x
    while x % i == 0: # check if i divides x
        #print(i)
        for a in range(2,i+1): # loop from 2 to i
            if i % a == 0 and i != a: # check if a divides i and i does not equal a
                break # break inner loop # exit loop if factor found

            else:
                print(i) # print i
                break # break inner loop

        x = x / i # divide x by i
        if i == 1 or i == 0: # if i is 1 or 0
            i = i + 1 # increment i

