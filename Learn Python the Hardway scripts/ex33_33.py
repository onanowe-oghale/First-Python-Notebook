def checkfunct (a , z):
    print("This program will add one to each number and create a list")
    a = a
    b = []
    while a < z:
        print("The top number is", a)
        print("We started with a list of", b)
        b.append(a)
        print("The new list is ", b)
        a +=3
        print("The bottom value is", a)
    print(b) 

    for r in b:
        print(r) 


x= input("Number which is less than - ")
y = input("Number which is limit value -")

checkfunct(int(x), int(y))        