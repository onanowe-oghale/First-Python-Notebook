from sys import argv
from os.path import exists

script , copyfrom , copyto = argv

print(f"We are about to copy from a file named {copyfrom} to a file named {copyto}")
print(f"The size of the input file is {len(copyfrom)} bytes")
print(f"The size of the output file is {len(copyto)} bytes")
newD = open(copyfrom).read() 

print("Our files should be ready to undergo the operation now to abort press ALT+F4 to continue press ENTER.")
input("> ")

print(f"Running a check to see if out file exists{exists(copyto)} Should Return true it does.")
finalD = open(copyto, 'w')
finalD.write(newD)

print("That should do it folk, GOODBYE!")
finalD.close