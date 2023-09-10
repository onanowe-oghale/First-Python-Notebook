#EX 6 : String and texts.

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "laravel"
do_not = "know Node"
y = f"Those who know {binary} and those who {do_not}."

print (x)
print (y)

print (f"I said: {x}")
print (f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny ?! {}"

print (joke_evaluation.format(hilarious))

w= "This is the left side of....."
e= "A string with a right side."

print (w + e)