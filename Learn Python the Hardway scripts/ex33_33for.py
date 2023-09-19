def inc_for (a , z):
    a = a
    b = []
    for num in range(a , z):
        print("This is the top number", num)
        b.append(num)
        print("Our list is now", b)
        print("The number below is now",num )

    print(b)
    for r in b:
        print(r)    


x = input("What number should be less than -")
y = input("What number is the limit - ")

inc_for(int(x) ,int(y))