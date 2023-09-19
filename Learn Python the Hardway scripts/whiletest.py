


def increment (a, z):
    num = a
    b = []
    while num < z:
        print("The number at the top is ", num)
        b.append(num)
        print("Our list then holds values", b)
        num=num+1
        print("At the bottom we have the number", num)
        

x = input("First number for loop to run -") 
y = input("What should be the limit - ")      
increment (int (x), int(y))