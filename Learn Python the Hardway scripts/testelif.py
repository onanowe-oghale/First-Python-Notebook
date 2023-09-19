#Barcelona quiz

print("This is a quiz on the catalan giants BARCELONA.\n")

print("Who was Barcelona's Keeper in the 2012 season")

print(""" 
Answers are:
      1. Valdes.
      2. Pinto.
      3. Ter Stegen.
      4. Bravo.
      5. Casillas.
      6. Lopez.
""")

answer = input("> ")

if answer == "Valdes" :
    print("Brilliant, that is correct \n")
    print("""Victor Valdes was in goal for Barcelona through 
          out Pep's reign at the club from 2008 - 2013 where he
          led the spanish giants to 2 UCL titles and a treble,
          Valdes was an integral part of these squads.
          """)
elif answer == "valdes":
    print("Check your spelling, name must start with Capital letter.")
    

elif answer == "Pinto" :
    print("""We will just allow you pass as Pinto was the second choice keeper
        Good thing you have an idea keep it up 👍""")
    
elif answer == "pinto":
        print("Check your spelling, name must start with Capital letter.")
    
elif answer == "Ter Stegen":
    print("Stegen is a Barcelona keeper alright but he wasn't the one in goal in 2012.")

elif answer == "ter stegen":
        print("Check your spelling, name must start with Capital letter.")

elif answer == "Bravo":
    print("Well...........")
    print("""You're sort of have an idea but Bravo was only the answer's sucessor
        not the goalkeeper at the time.
""")   

elif answer == "Casillas" or "Lopez":
    print("Oops that's wrong that's totally off the mark. TRY AGAIN !")         
             
else:
    print("Well, try again. Ensure it is being spelt correctly as the options show.")  
    
  