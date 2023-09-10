#imports argv from system module
from sys import argv 

#the the two variables named from the argv
script, filename = argv

#Prints the the messgae and inputs the filename being passed as argument in the terminal calling it from the argv
print(f"Were going to erase {filename}")

#Prints the message asking if the user of the application wishes to go ahead with erasing the file and prompts on what the  user should do if they do not wish to. 
print("If you don't want that, hit CTRL-C (^C).")

#Prints a message containing information on what to do go on with the file to be erased
print("If you do want that, hit RETURN.")

#Waits and collect input from user on whether to choose that particular file for erasing.
input("?")

#Prints the message that the file is getting open
print("Opening the file...")

#opens the file for erasing in the variable and assigns it to variable lip
lip = open(filename, 'w')

#prints the message truncating the file
print ("Truncating the file. Goodbye!")

#Erases the content of the file in variable filename
lip.truncate()

#Prints the message for informing that it will ask for three lines.
print("Now I'm going to ask for the three lines.")

#Collects input for line 1 and saves it in a variable line1
line1 = input("line 1: ")

#Collects input for line 1 and saves it in a variable line2
line2 = input("line 2: ")

#Collects input for line 1 and saves it in a variable line3
line3 = input("line 3: ")

#Prints the message that it is going to write the inputs collected and take into that file which was truncated.
print("I'm going to write these to the file.")

"""#Writes the input from line1 which we collected in input to the first line of the  file.
lip.write(line1)

#takes the writing to the next line
lip.write("\n")

#Writes the input from line2 which we collected in input to the second line of the file.
lip.write(line2)

#takes the writing to the next line
lip.write("\n")

#Writes the input from line3 which we collected in input to the third line of the file.
lip.write(line3)

#takes the writing to the next line.
lip.write("\n")
"""

#Shorter way to print  
#assign the format string with contents on variables line1, 2 and 3 the variable short
shorts = f"{line1}\n {line2}\n {line3}\n"

#writes the input from each line stored in each variable and the \n takes it to the next line.
lip.write(shorts)

#prints the message that it's about to get closed.
print("And finally, we close it.")

#closes the file.
lip.close()