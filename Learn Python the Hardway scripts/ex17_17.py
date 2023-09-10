#Trying to make the code much smaller.
#This line imports the argument variable from system module.
from sys import argv

#Imports the exists command from the os.path
from os.path import exists

script , fileA , fileB = argv

print(f"We will be copying {fileA} to {fileB}")
indata = open(fileA);new_build = indata.read()


print(f"the input file is {len(new_build)} bytes long.")

print(f"The Output file {exists(fileB)}")
print("Want to proceed tap ENTER now or close with ALT + F4.")
input("$ ")

out_file = open(fileB, 'w')
out_file.write(new_build)

print("We're done here now!")
out_file.close()