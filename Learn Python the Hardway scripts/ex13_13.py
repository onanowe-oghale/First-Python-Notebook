'''from sys import argv

script , costly, breathe = argv

print("The name of this script is", script)
print("The price to be paid for this application is hidden in the variable", costly)
print("The details of the current Nigerian Government are embedded in the variable", breathe)

#When given lesser than three arguments it gives an error message of accepting 4
#When given fewer or more arguments than it should have the code does not run as it expects the specific amount of arguments needed.
'''

from sys import argv

script ,  major_p , hard_p , word_p = argv

print("What is the most common programming language ?")
major_p = input()

print("What are some of the hard programming languages out there ?")
hard_p = input()

print("What are some programming languages you would not advice one to use ?")
word_p = input()

print("The name of the script is", script)
print("The most common programming languages are", major_p)
print("Languages like", hard_p, "are not easy to learn")
print("Actual beginners in my opinion should steer clear of languages like", word_p)