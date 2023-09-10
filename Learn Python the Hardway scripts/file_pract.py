from sys import argv

script , filename = argv

print(f"We're going to wipe out everything in {filename}")
print("If you dont not wish to go ahead with the wipe hit CTRL + W")
print("If you wish to go ahead, hit RETURN")
input("> ")


print("We're Opening the said file now.....")
build = open(filename, 'w')

print("We're about to truncate the same file now.... ADIOS")
build.truncate

print("Now I'm going to ask for three line")
line1 =  input("LINE 1: ")
line2 =  input("LINE 2: ")
line3 =  input("LINE 3: ")

print("I'm going to write these to the file")

new_file = f"{line1}\n {line2}\n {line3}\n"

build.write(new_file)

print("Then we close the file.")
build.close