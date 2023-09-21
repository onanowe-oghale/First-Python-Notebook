# this is a reincarnation of the bear game

from sys import exit

def gold_room():
    print("Welcome into the room filled with gold")
    print("""How much gold would you like to take ?
          \t Choose Wisely!
          """)
    
    choice = input("-Intending Gold Amount > ")
    if  "1" in choice or "0" in choice:
        how_much = int(choice)
    else:
        print("I Don't quite get that !")

    if how_much < 50:
        print("Now, that's good Congratulations you win.")
        exit(0)
    else:
        dead("You greedy bastard")


def bear_room():
    print("You have stepped into the Bear's Lair")
    print("The Bear has a pot of honey")
    print("The Bear stands between you and the door to impossibilities")
    print("What will you do choose wisely.....")
    bear_moved = False
    while True:
        bear_choice = input("> ")
        if bear_choice== "take honey":
            dead("Bear looks at you and slaps you")

        elif bear_choice == "taunt bear" and not bear_moved:
            print("That's Wise")
            print("The Bear steps away from the door.")
            bear_moved = True

        elif bear_choice== "open door" and bear_moved:
            print("Openint the door")
            gold_room()

        elif bear_choice== "taunt bear" and bear_moved:
            dead("Bear Devours you.")

        elif bear_choice== "stare"  and bear_moved:
            print("Bear slaps you to the beginning")
            start()

        else:
            print("I don't quite get that")


def volcra_room():
    print("You have entered the room of the dangerous volcra")
    print("The Volcra is moving towards you with speed")
    print("Do you flee or let it have you head")

    volcra_choice = input(">")

    if "flee" in volcra_choice:
        print("You run at full speed from the volcra!")
        start()
    elif "head" in volcra_choice:
        print("OOPS") 
        dead("The Volcra has you head.....")
    else:
        print("I didn't quite get that.")
        volcra_room()


def dead(why):
    print(why, "That's Goodbye Folks, Good one.")
    exit(0)

def start():
    print("You're in a mysterious dark house")
    print("You can turn either left OR right to continue in the game.")
    start_choice = input("> ")

    if "left" == start_choice:
        print("Accessing you decison")
        volcra_room()
    elif "right" == start_choice:
        print("Please wait")
        bear_room()
    else:
        print("Can't quite get that.") 
        start() 


start()
