# this is a function that allows you to read the contents of a file

from sys import argv
script , file_name = argv

def total(f):
    print(f.read())

def start(f):
    f.seek(0)

def each_line(lines , f):
    print(lines , f.readline(),end="")            

current_file = open(file_name)

print("This shows the full txt file")

total (current_file)

print("This takes us to the beginning of the file O Bytes position \n")

start(current_file)

print(f"We will now read each line in {script} one by one")

line_num = 1
each_line(line_num , current_file)

line_num += 1
each_line(line_num , current_file)

line_num += 1
each_line(line_num , current_file)
