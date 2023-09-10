#imports the argument variable from the system module
from sys import argv

#these are two variables names from the argv
script , input_file = argv

#makes a function holds the variable f which is a file that and names in print_all
def print_all(f):
#this line of code makes the function to read the file and prints the content of the file as output   
    print(f.read())

#makes a function that and is named rewind
def rewind(f):
#this line of code maoves the file while to be read from 0 bytes.    
    f.seek(0)

#makes a function that is named print_a_line taking two arguments of line_count(this is an integer that represents the line number) and the file object:f
def print_a_line(line_count, f):
#This f.readline() reads a single line and the print statement prints bothe the line number and the content of the line.    
    print(line_count, f.readline())

#opens the file in the second variable and assigns it to the variable current_file
current_file = open(input_file)

#Gives out the message  after the first " before the \n. The \n makes the line go to the next.
print("First let's print the whole file:\n")

#Calls the function print all and puts the argument which is the current file this
print_all(current_file)

#prints out the message Now let's rewind, kind of like a tape.
print("Now let's rewind, kind of like a tape.")

#calls the function rewind which seeks the file back to its first bytes. whilst passing the current_file variable as argument
rewind(current_file)

#Prints the message let's print three lines.
print("Let's print three lines:")

#makes the current line on display to be one
current_line = 1 #(current line here is equal to one: the first line)
#this prints out the line number starting at one and from the readline function prints everything on the first line as the rewind function has taken out cursor to the beginning.
print_a_line(current_line, current_file)

#makes the current line on display to be plus one which would be two.
current_line = current_line + 1 #(current line here is equal to two: the second line)
#this prints out the line number which would increase by two due to what the current file variable holds and it also prints the second line in the file
print_a_line(current_line, current_file)

#makes the current line on display to be plus one which would be three.
current_line = current_line + 1 #(current line here is equal to three: the third line)
#this prints the next line numer which would increase to three as the previous did by one it also prints the next line of the function.
print_a_line(current_line, current_file)

#--------------------------------Python the hardway exercise 20.------------------------------------

#the reason why the current_line increases is because we  keep adding 1 to it after establishing it's first value as one.
#the value line count variable from the print_a_line function is connected to the variable current_line. The line_count argument holds place for the current_line variable later used the same way the f argument which in function is told to print file singular lines holds the current_file variable later used. 

# using the += operator we can write our code as 

current_line += 1