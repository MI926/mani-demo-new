x = input("Enter a string: ")
print(x[::-1])
y = ""
for i in x:
    o = i
    match o:
        case 'b':
            y = y + 'd'
            continue
        case 'd':
            y = y + 'b'
            continue
        case 'i':
            y = y + 'i'
            continue
        case 'x':
            
            y = y + 'x'
            continue
        case 'o':
            y = y + 'o'
            continue
        case 'v':
            y = y + 'v'
            continue
        case 'w':
            y = y + 'w'
            continue
    y = y + i

print(y) 
    

