#makes a variable i and stores a value if 0 in it.
i = 0

#makes a variable called numbers and  assigns an empty list to it
numbers = []

#this makes a loop which says that as far as the number in i is less that 6 the block of code should be executed
while i < 6:
#prints the message with the formatted string  variable i storing I's current number    
    print(f"At the top is {i}")
#this adds the new value of i to the list    
    numbers.append(i)
#this adds 1 to the already existing number in i    
    i = i + 1
#this prints out a string with the variable number which now has a value inside and a new value added by one    
    print("Numbered now:", numbers)
#this prints out a string that tells us the new value being added to our list.    
    print(f"At the bottom i is {i}")
#The entire block of code above runs till the number is equal to 6.....

#this prints a message that about the number.
print("The numbers: ")

#a loop which checks through the content in the the numbers variable
for num in numbers:
#prints all the contents in the numbers variable which have now been stored in the num variable.    
    print(num)