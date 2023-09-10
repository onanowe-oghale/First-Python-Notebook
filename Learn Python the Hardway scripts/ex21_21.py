#this line makes a function and names it add whilst passing two arguments a and b
def add(a , b):
#this display what the function is doing in this case it is adding two numbers.    
    print(f"ADDING {a} + {b}")
#this returns the result of adding a and b back to the function    
    return a + b
#this line makes a function and names it subtract and passes two arguments a and b
def subtract (a, b):
#this line prints out what the function does in this case it subtract two numbers a and b    
    print(f"SUBTRACTING {a} - {b}")
#this returns the result of subtracting a from b to the function    
    return a - b

#this line makes a function and names it multiply it also passes two arguments a and b
def multiply (a, b):
#this line gives out a message on what exactly the function is doing in this case it is multiplying two number    
    print(f"MULTIPLYING {a} X {b}")
#this returns the result of multiplying a and b back to the function.   
    return a * b
#this line makes a function and names it divide also passing two arguments a and b
def divide (a, b):
#displays the message of what exactly the function does which is dividing two number    
    print(f"DIVIDING {a} / {b}")
#this returns the result of dividing a by b back to the function.    
    return a / b

#displays the message Let's do some math with just functions.
print("Let's do some math with just functions!")

#this uses the result made by the return function which adds two number the arguments are passed and the result gotten is stored in variable called age.
age = add(30, 5)
#this uses the result from the subtract function to subtract two numbers 78 being a and 4 being b it then stores its result in the variable height.
height = subtract (78, 4)
#this uses the multiply function which multiplies two number 90 being a a 2 being b in this case, the result is then stored in the variable called weight.
weight = multiply(90, 2)
#this uses the function divide which accepts two arguments and divides two number the result is saved in the variable iq.
iq = divide(100, 2)

#this prints out the result from the operations done with use of the function and the arguments passed which have all been stored in variables
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#this prints out the message that here is a puzzle.
print("Here is a puzzle.")

#---------------------------------------------------------------------------------------------------------
#this line of code takes the values already gotten from the operations with the arguments given it calls the divide function on iq and 2 which gives an output of 25 = 50/2
#then it uses the function multiply which multiplies two numbers to multiply the contents of the variable weight and value gotten from dividing out iq variable by 2.
#the it is all written in the function subtract. And that is a function that subtracts two numbers so it subtracts the value in the variable height from the value gotten when the multiply function works on iq/2 and the value in variable weight.
#the main paranthesis that covers the entire function makes it to add two numbers, it adds the variable result in age to the value gotten from dividing iq variable by 2 then multiplying it by the weight variable and subtracting the new value from the height variable. 

#notice that there is no only a single main comma that seperates the two main arguments which are age and what is in the subtract function.
#this is then stored in the variable what.
What = add(age, subtract(height, multiply(weight, divide(iq, 2))))
from_ex = divide(add(24 , 34) , subtract(100 , 1023))
#prints out the result gotten from the operation.

print("That becomes:", What, "Can you do it by hand")
print("24 + 34 DIVIDED BY 100 - 1023 is" ,from_ex)