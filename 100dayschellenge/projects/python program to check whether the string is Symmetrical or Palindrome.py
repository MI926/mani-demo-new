def similar_string_find(a):
    if a[::-1] == a:
        print("yes it is palidrome")
    else:
        print("its not a palidrome")  
x = input("enter name") 
similar_string_find(x)         