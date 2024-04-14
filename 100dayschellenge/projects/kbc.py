l = {("What is the capital of India?", ("Bangkok", "Washington DC", "Dubai", "New Delhi"),
      (4)), ("Who founded the Azad Hind Fauj?", ("Netaji", "Gandhiji", "Pandayji", "Arbindo"), (1)),
     ("What is the national animal of India?", ("Tiger", "Lion", "Elephant", "Peacock"),
      (1)), ("Who is the prime minister of India?", ("Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Manmohan Singh"),
             (1)),
     ("Which is the largest state in India?", ("Rajasthan", "Madhya Pradesh", "Uttar Pradesh", "Maharashtra"),
      (3)),
     ("Which is the largest desert in India?", ("Thar Desert", "Rann of Kutch", "Ladakh", "Sundarbans"),
      (1))}

c = 0
for i in l:
    print(i[0])
    a = 1
    for j in i[1]:

        print(a, j)
        a = a + 1
    b = int(input("chosse the options."))
    n = 1
    if b == i[2]:
        print("correct you won")
        if n == 1:
            c = c + 5000
            n = n + 1
        elif n % 2 == 0:
            c = c * 2
            n = n + 1
        elif n % 3 == 0:
            c = c * 20
            n = n + 1
print(c)