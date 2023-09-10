#Prompting and Passing

from sys import argv

script, user_name , job = argv
topboy = '^ '

print("What Username would you like to use ? ")
user_name = input()

print("What do you do you do for a living")
job = input()

print(f"Hi {user_name}, I'm the {script} script.")
print(f"I'd like to ask you a few questions. I already know you are a {job}")
print(f"Do you like me {user_name}?")
likes = input(topboy)

print(f"Where do you live {user_name}?")
lives = input(topboy)

print("What kind of computer do you have?")
computer = input(topboy)

print(f"""
    Alright, so you said {likes} about liking me.
    You live in {lives}. Not sure where that is.
    And you have a {computer} computer. Nice.
      """)