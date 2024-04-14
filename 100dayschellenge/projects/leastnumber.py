

'''x = input("Enter the string")
z = list(x)
m = []
for i in z:
    k = z.count(i)
    #print(k)
    e = [(i, k)]
    m.extend(e)
    #print(i)
#print(m)
g = []
for i in m:
    if i not in g:
        g.append(i)

c = 0
q = ""

print(g)
'''
for i in g:
    #print(i)
    lrtf = i[1]
    if lrtf <= len(x):
        c = i[1]
        q = i[0]
print(q)
x = input("Enter the string: ")

# Count occurrences of each character in the input string
char_count = {}
for char in x:
    char_count[char] = char_count.get(char, 0) + 1

# Find the minimum count
min_count = min(char_count.values())

# Find all characters with the minimum count
min_chars = [char for char, count in char_count.items() if count == min_count]

if min_chars:
    print(f"The character(s) with the minimum occurrence ({min_count} times) in the input string are: {', '.join(min_chars)}")
else:
    print("No characters found in the input string.")
