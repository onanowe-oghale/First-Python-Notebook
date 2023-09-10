# this is a simple function to calculate simple interest using the return function

def add_line (x , y):
    return int(x + y)

def multiply_line (x , y):
    return int(x * y)

def division_line (x , y):
    return int(x / y)

def subtraction_line (x , y):
    return int(x / y)

#The formula for simple interest is given as PRT / 100
print("This program calculates simple interest for MORBID BANK P.L.C Atlantis")
principal = float(input("The principal - "))
rate = float (input ("At what rate - "))
Time = float(input("What is the stipulated amount of time in years NOTE:(IN YEARS) - "))

#This might seem ambigious as there are easier ways to do this but this all for the sake of understanding functions

S_I = division_line(multiply_line(principal, (multiply_line(rate, Time))), 100)

print(f"Our simple interest with an investment of {principal} at a rate of {rate}% for {Time} years at MORBID BANK is :\n {S_I}")

print("Do you wish to calculate amount ? Press ENTER to continue")
input ("> ")


#Amount is = Principal + Simple Interest.......
Amount = add_line(principal , S_I)
print(f"The total amount gotten from MORBID BANK is: {Amount}")