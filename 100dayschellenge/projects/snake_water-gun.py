
l = {"Snake", "Water", "Gun"}
x = l.pop()
while True :
    print('''
          Enter The Value. 
            1 For Snake
            2 For Water
            3 for Gun
      
       ''')
    user = int(input("Enter the value"))
    
    match x:    
        case "Snake" if user == 1:
            print("tie")
        case "Snake" if user == 2:
            print("you win")
        case "Snake" if user == 3:
            print("I win you Loose the match")
        case "Water" if user == 1:
            print("I win you Loose the match")
        case "Water" if user == 2:
            print("tie")
        case "Water" if user == 3:
            print("you win")
        case "Gun" if user == 1:
            print("you win")
        case "Gun" if user == 2:
            print("I win you Loose the match")
        case "Gun" if user == 3:
            print("tie")
        case _:
            print("Please Try Again and Enter Right Value")

    print(x)
    #print("Press Enter if you want to Continue The Game")
    user1 = input("Press Enter if you want to Continue The Game")
    
    if user1 == "":
        pass
    else:
        break