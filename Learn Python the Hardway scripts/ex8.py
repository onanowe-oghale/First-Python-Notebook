#Ex. 8 :Printing, Printing

#formatter variable containing 4 sets of {}
formatter = "{} {} {} {}"

#print statement replaces prints a whole new string which changes what is in the variable formatter with four other values using the format string capability
print(formatter.format(1, 2, 3, 4))

#print statement replaces prints a whole new string which changes what is in the variable formatter with four other values in this case strings one two three and four using the format string capability
print(formatter.format("one", "two", "three", "four"))

#print statement replaces prints a whole new string which changes what is in the variable formatter with four other values in this case boolean values True False False True  using the format string capability
print(formatter.format(True, False, False, True))

#print statement in which the original formatter variable is formatted and replaced with fours sets of the values in the variable as we can see each formatter var contains 4 {} which are now 16 due to the format string
print(formatter.format(formatter, formatter, formatter, formatter))

#print statement in which the format string containing four set of strings changes what is in the original formatter variable to be printed.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "or a song about fear"
))