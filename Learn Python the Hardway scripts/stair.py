# stair challenge python builder.
print("Welcome to the Mystery house challange!")
print("Please what is your name ?")
name = input("What is your name: ") 

print(f"""
    Alright {name} You are trapped in a mystery house and you need to get out immediately
    There's a staircase right infront of you and a magical locked door east of the house
    One way leads to you leaving with wealth, the other let's you leave but empty handed.
    Be careful what you choose.
""")


print("""
Choose 1 To climb the stairs
Choose 2 to go to the East of the house.
""")

print("Put the number you wish to put in")
answer = input("> ")

if answer == "1":
    print("Climbing the stairs then.")
    print("Just climbed the stairs to the end")
    print("""
        There 3 are rooms around you.
        Press 1 to enter the first room. 
        press 2 to enter the second room.
        press 3 to enter the third room. 
          """)
    
    stairs = input("> ")

    if stairs == "1":
        print("Wow, look at the gold in front of you.")
        print("""
             Press 1 to pick gold
             press 2 to just close the door
              """)
        
        Door1 = input("> ")
        if Door1 == "1":
            print("The Dragons descends to tear you apart")
            print("You should not toy with his gold.")

        elif Door1 == "2":
            print("Good thing, you didn't let greed get you.")
            print("Now you have teleported to the beginning of the game.")

        else:
            print("Well that's a wrap, we're going back to the beginning.")   


    elif stairs == "2":
        print("Before you lies a dusty book as you open the door")
        print("Oh look there's a Nintendo switch on the left of the room")
        print(""" 
            Press 1 to pick the dusty old book and open it
            Press 2 to pick the Nintendo switch
        """)             

        Door2 = input("> ")

        if Door2 == "1":
            print("""
                Congratulations you have gotten the formula for Eternal wealth
                You have conquered the monster house and you're free.
            """)

        elif Door2 == "2":
            print("""
                Taking the Nintendo switch was a huge mistake you'll be trapped here for 5 years.
            """)  
            print("Goodbye!")

        else:
            print("When there is a will there is a way keep trying there is a way out.")   

    elif stairs == "3":
        print("This room seems empty nothing here can lead us out")
        print("""
            We can only do 2 things here
            we can rest and strategize or go back and to the beginning and keep looking!
              """)
        print("""
            Press 1 to rest and strategize your way out.
            press 2 to go back to the beginning and try again.  
        """)           

        Door3 =input("> ")
        if Door3 == "1":
            print("""
            Alright then, REST..............................
            """)
            print("Alright we are back at the beginning.")

        elif Door3 == "2":
            print("The answer's will come in time keep looking")  

        else:
            print("You'll always figure it out. Don't Worry.") 

elif answer =="2":
    print("At the east of the house lies a door with a Magic word needed to open it")
    print("HINT: It is one of the five magic words you know.")

    print("Input the Magic Word")
    word = input("> ")

    if word == "Please":
        print("Congratulations! you are now free from the shakcles of the mystery house.")

    elif word == "please":
        print("Check your spelling and ensure it starts with a capital letter.")

    else:
        print("""Without the Magic word you can't pass
              Hint: Ensure it's been spelt correctly with first letter as capital,
              We are going back to the beginning""")    
        
else:
    print("You dont want to remain trapped do you ? Keep trying.")        
