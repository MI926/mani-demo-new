import random
random.seed(250)
a = []
for i in range(0, 1000000):
    b = random.randrange(0, 2)
    #print(b)
    a.append(b)
#print(random.randrange(0, 1))
#print(a)

# Generate a list of random numbers
random_numbers = a
"""for i in range(64):
    random_numbers.append(random.randrange(0, 2))
print(random_numbers)"""
# Try to find the seed value by checking all possible seeds
for seeds in range(0, 2000):
    #print(seeds)
    random.seed(seeds)
    test_numbers = [random.randrange(0, 2) for _ in range(1000000)]
    #print(test_numbers)
    if test_numbers == random_numbers:
        print(f"The seed value is: {seeds}")
        break
else:
    print("Could not find the seed value.")
