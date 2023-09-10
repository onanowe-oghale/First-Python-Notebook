# function to print the club's champions league title's

#this line defines the function and calls it european giants passing two arguments of club1 and club2
def european_giants(club1 , club2):
    #prints the a message on the amount of ucl titles Bayern have with a format string from the argument to update the number 
    print(f"Bayern have {club1} UCL titles")
    #prints the a message on the amount of ucl titles Barca have with a format string from the argument to update the number 
    print(f"Barcelona have {club2} UCL titles")
    #prints they are both big level clubs
    print("They are both big level clubs.")
    #prints out the message in the paranthesis
    print("But Real madrid is the biggest.")
    #prints out the message in the paranthesis
    print("We go onto the next.\n")

#print a message that we are giving our function number's
print("Giving our function the number's directly")
#takes the function named european_giants and passes the values 6 and 5 into the arguments
european_giants(6 , 5) #information given here at output is true as of 2023 

#use variables
#prints the message in the parathesis
print("Then we make use of Variables")

#creates a variable and assigns the value on the right to the left
clubOne = 6
clubTwo = 5

#assigns the variables just recently to the function european giants as arguments
european_giants(clubOne , clubTwo)

#Use operations in them as well.
#prints the message in the paranthesis
print("We can run mathemtical operations in them as well.")
#line of code performs mathematical operation for the function and then passes it as argument
european_giants(3 + 3 , 10 - 5)

#Combination of Variables and Math
#prints the mesaage within the paranthesis and quotation marks
print("We try to combine Variables and Math.")
#calls the function european_giants and passes the variables alongside some mathematical operation as our arguments.
european_giants(clubOne + int (6 / 2) - int(3), clubTwo + int (5 / 2)- int(2.5)) #information from this may not be correct



#all information here is true as at september 2023