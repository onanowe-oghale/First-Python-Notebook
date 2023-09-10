#this one is like the scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#That *isnt worth it we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this makes just a single argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this function would take no arguments
def print_none():
    print("I do not contain anything'.")            


print_two("Oghale", "Baruch")
print_two_again("Oghale","Baruch")
print_one("First!")
print_none()