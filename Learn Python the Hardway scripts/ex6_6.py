#Study srill for EX 6

#makes a variable types of people and assigns a value of 10 to it
types_of_people = 10

#makes a variable x which contains a format string in which out previous variable types of people can come in
x = f"There are {types_of_people} types of people."

#makes a variable binary to store the string binary
binary = "binary"

#makes a variable do_not to store the string don't
do_not = "don't"

#makes a variable y which contains a format string which puts values binary and do_not into this new string
y = f"Those who know {binary} and those who {do_not}."

#This prints out out x variable 
print (x)

#This prints out our y variable
print (y)

#This print statement prints out a string in which one of our previous variables x is being invoked using format string
print (f"I said: {x}")

#This print statement prints out a string in which one of our previosu variables y is being invokes using format string
print (f"I also said: '{y}'")

#makes a variable called hilarious and gives it a value of False
hilarious = False

#makes a variable called joke_evaluation and store string valur Isn't that joke so funny and opens up a format string to be used later
joke_evaluation = "Isn't that joke so funny ?! {}"

#Prints out the format string value in variable hilarious after printing the value stored in variable joke_evaluation
print (joke_evaluation.format(hilarious))

#stores string "This is the left side of....." in the variable named w
w= "This is the left side of....."

#stores string value A string with with a right side in variable
e= "A string with a right side."

#prints both variables above w and e with the help of the + operator
print (w + e)