from sys import exit

def gold_room():
    print("In here lies a massive pot of gold")
    print("How much gold do you wish to collect")
    print("Choose wisely.")

    choice = input("Amount of gold > ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        print("Man what are you typing ?")

    if how_much < 50:
        print("That is great, you win man")
        exit(0)
    else:
        dead("you greedy bastard!")


def bear_tunnel():
    print("You have just entered the bear's lair")
    print("The Bear has a huge pot of honey in it's possesion")
    print("The The bear stands between you and the door")

    bear_moved = False
    while True:
        choice = input("What do you do about the Bear ? > ")
        if "take honey" in choice:
            dead("Bear looks at you and slaps you.")

        elif "taunt bear" in choice and not bear_moved:
            print("Now the bear has moved away from the door")
            print("Nothing stands between you and the door now")
            bear_moved = True

        elif "taunt bear" in choice and bear_moved:
            dead("Bear proceeds to devour you!")

        elif "open door" in choice:
            print("Evaluation Your Decisons")
            gold_room()    

        elif "stare" in choice and bear_moved:
            print("Bear pushes you away.")
            start()

        else:
            print("I don't accept that.")  


def volcra_room():
    print("You have just entered the volcra's domain.")
    print("The volcra is slowly advancing towards you.")
    print("You can either flee or let in have your head")

    choice = input("> ")
    if "flee" == choice:
        print("Good one")
        start()
    if "head" == choice:
        dead("Yummm, the volcra has your head.")



def dead(why):
    print(why, "That ends it, Goodbye.")
    exit(0)

def start():
    print("You are in a mysterious dark house")
    print("There are two ways to go")
    print("Choose one left OR right") 
    choice = input(">")

    for            

