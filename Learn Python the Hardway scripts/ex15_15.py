"""#This line imports the argument variable form the system module
from sys import argv 

#This unpacks the elements of the argv list into two variables which are script and filename.
script, filename = argv

#opens the file specified by filename varianle and assigns the resulting file object to the variable txt
txt = open(filename)

#Prints the the Here's your file with the format string which the is enabled by the f in front of the first quotation mark in the print statement allowing the values in the variable filename to be printed.
print(f"Here's your file  {filename}:")
#prints the content of the file that which was assigned a variable of txt
print(txt.read())

#Prints out a prompt to input a filename again.
print("Type filename again: ")

#the input on the right side of the code below this line accepts the name of the new file to be displayed and stores it in a variable file again.
file_again = input("//- ")

#the right side of the code helps us to open our file which was assigned the variable and then stores the it in a variable txt again.
txt_again = open(file_again)

#prints out the content of our file txt again
print(txt_again.read())
"""


"""#Code with no lines 10- 15
from sys import argv 

script , thefile = argv

jump = open(thefile)

print(f"Here's your {thefile}: ")
print(jump.read())
"""

#lines 10-15 INPUT

print("Input A File Again: ")
thenew =  input("> ")

fileopen = open(thenew)
print(fileopen.read())