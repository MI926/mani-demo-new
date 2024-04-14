from ast import match_case


x = input("enter the string:- ")
y = x.split(" ")
z = ""
for i in y:
    match i:
        case "zero":
            z = z + "0"
        case "one":
            z = z + "1"
        case "two":
            z = z + "2"
        case "three":
            z = z + "3"
        case "four":
            z = z + "4"
        case "five":
            z = z + "5"
        case "six":
            z = z + "6"
        case "seven":
            z = z + "7"
        case "eight":
            z = z + "8"
        case "nine":
            z = z + "9"
        case "ten":
            z = z + "10"
print(z)
