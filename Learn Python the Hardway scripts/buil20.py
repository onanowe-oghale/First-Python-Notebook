from sys import argv

script , theFile = argv

def entire_print(f):
    print(f.read())

def beginning(f):
    f.seek(0)

def line_print(line_no, f):
    print(line_no, f.readline())

filely = open(theFile)

print("Now we print the whole file.\n")

entire_print(filely) 

print("We then fly to the beginning of the file in question")

beginning(filely)

print("We'll print line by line from the beginning!")

theline = 1
line_print(theline, filely) 

theline += 1
line_print(theline, filely)

theline +=1
line_print(theline, filely)