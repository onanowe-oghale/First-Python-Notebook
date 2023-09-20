from sys import exit

def gold_room():
    print("this room room is filled with gold!")
    print("How much gold do you wish to carry ?")
    number = input("> ")

    if "0" in number or "1" in number:
       how_much = int(number)
    else:
        print("Man, learn how to type.")

    if how_much < 50:
        print("You're a good lad, you win")
        exit(0)
    else:
        dead("You greedy bastard")  



def bear_way() :
    print("Now you've entered the bear's lair")
    print("The bear has a pot of honey and is blocking the door")
    print("What will you do ?")
   

    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("Bear looks at you and slaps your face!")

        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved away from the door")
            print("Now you can move")
            bear_moved = True

        elif choice == "taunt bear" and bear_moved:
            dead("Bear devours you.")

        elif choice == "open door" and bear_moved:
            print("This leads to the gold room.")
            gold_room()

        else:
            print("I don't quite understand that .")    


def volcra_room():
    print("You have stepped into the lair of the dangerous Volcra")
    print("The volcra is coming towards you")
    print("What will you do flee or let him have your head.")
    choice = input("> ")

    if "flee" in choice:
        print("You took to your heels from the volcra.")
        start()

    elif "head" in choice:
        print("wow!")
        dead("Head was quite tasty.")

    else:
        print("Not a valid move")
        volcra_room()    

def dead(why):
    print(why, "That ends it , Good bye") 
    exit(0)           

def start():
    print("You are in a cold dark room")
    print("There are two ways to be taken.")
    print("There is left and there is right.")

    choice = input("Which way do you intend to go >")    
    if "right" in choice:
        print("Getting your decison accepted")
        bear_way()

    elif "left" in choice:
        print("Getting your decision accepted")
        volcra_room()
    else:
        dead("You stumble around in the dark in fall.")

start()                                      