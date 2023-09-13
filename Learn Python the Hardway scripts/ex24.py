#prints all messages in the paranthesis and quotation marks
print("Let's practice everything.")
print('You\'d need to know \'about escapes with \\ that do:')
print('\n newlines and \t tabs.')

#names a variable poem with triple quotes which allow multiple line prints acceptbale without indentation
poem = """
\t The lovely world
with logic so firmly planted
cannot discren \n the need of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

#prints everything available in the paranthesis and the quotation marks
print("---------")
#prints the content of the variable poem
print(poem)
#prints everything available in the paranthesis and the quotation marks
print("---------")

#calculates the operation on the right and assigns it's result to the left
five = 10 - 2 + 3 - 6

#prints out the result with some string
print(f"This should be five : {five}")

#defines a function and passes a single argument
def secret_forula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans , jars , crates

start_point = 10000

#makes a variable that would take the place of the values returned from the operations made in the function
beans , jars , crates = secret_forula(start_point)

#remember that is another way to format a string
print("With a starting point of: {}".format(start_point))

#it is also like using this and f "" string
#prints the values directly gotten from the operation and into the variables along with the string
print(f"We'd have {beans} beans, {jars} jars and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_forula(start_point)
#this is an easy way to apply a list to a format string

#uses string formatting to unpack the values from the tuple into the format function
print("We'd have {} beans, {} jars, and {} crates".format(*formula))