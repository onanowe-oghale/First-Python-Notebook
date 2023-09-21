#This is a text based game about helping Neymar to win the Balon d'or

from sys import exit

#username prompt
username = input(">Input Your Username> ")

#game beginning message
print(f"""\t Welcome {username} 
    Neymar is one of the best talents the 
    game of football has ever seen we'll be helping him
    in our quest today to win the Balon d'or """)

#world cup finals 1st half
def Wc_finals_Half1():
    print(f"Congratulation {username} with you help Neymar is happy.")
    print("Neymar has successfully moved through the knock out stage with Brazil")
    print("It's the world cup final now")
    print("What do we do ?")
    print("start or kick off")

    Wc_finals_Choice = input("Choose what to do > ")
    if "kick off" in Wc_finals_Choice:
        print("Now we are live")
        print("It's the 36th minute Paqueta puts Neymar through on goal")
        print("He's one on one with the keeper where does he slot it")

        choicewc1 = input("> top or bottom corner >  ")
        if "top corner" in choicewc1:
            print("Brazil take the lead it's 1-0")
            print("Brazil head into half time with the lead.")
            Wc_finals_Half2lead()
        elif "bottom" in choicewc1:
            GK_saved()
            Wc_finals_Half2()
        else:
            print("I DIDN'T QUITE GET THAT.")
            Wc_finals_Half1()
    else:
        print("Start the final with kick off")
        Wc_finals_Half1()
#wc outcome 1 world cup finals with the lead at half time
def Wc_finals_Half2lead():
    print("We're back for the second half Brazil are in the lead")        
    print("It's the 58th minute Neymar wins a freekick on the edge of the box")
    print("Should Neymar take it ?")
     
    print(""" 
         eligible takers include:
          Raphinha
          Rodrgyo
          Paqueta
          Vanderson
    """) 
    freekick_player = input("Who steps up to take the freekick ? ")
    if "neymar" in freekick_player:
        print("Ney could double brazil's lead here")
        print("This could be game set and match, he's on the left side of the box")
        print("Where should he place it ?")

        fk_ney = input("top right or top left ? > ")
        if "top right" in fk_ney:
            print("GOOOAALLLLLL Brazil are almost there")
            print("It's a brace for Neymar!")
            print("We are into stoppage time now.")
            print("Referee looks at his watch")
            print("Brazil win 2 - 0")
            WC_won()
        elif "top left" in fk_ney:
            print("Ouch, it just skims the bar")
        else:
            print("Could not quite get that....") 
            Wc_finals_Half2lead()
    elif "paqueta" in freekick_player:
        print("Paqueta shapes to take...")  
        paqu_choice = input("Where should he place it > ")
        
        if "top right" in paqu_choice:
            print("Brazilllllll, GOOOOAAALLLLLLLL")
            print("We are into stoppage time now.")
            print("Referee looks at his watch")
            print("Brazil win 2 - 0")
            WC_won()
        else:
            print("It sails horribly wide")
            WC_won_by1()

    elif "raphinha" or "rodrygo" or "vanderson" in freekick_player:
        print("Sails horribly wide.")   
        WC_won_by1()
    else:
        print("Sorry couldn't quite get that....")
        Wc_finals_Half2lead()  

#wc outcome 2 halftime without the lead.....
def Wc_finals_Half2():
    print("We're back for the second half and brazil are tied in the World cup finals.")
    print("It's really tense here in the arena.....")
    allison_saves()

    print("Paqueta is through on Goal brilliant pass from Neymar")
    print("Paqueta shoot----")
    GK_saved

    print("it's a corner for Brazil")
    print("Raphinha takes, Angelo Santos header")
    GK_saved

    print("Neymar skips from 2 skips from 3")
    print("Trys to find the top corner")
    GK_saved

    print("Into the dying minutes now and brazil are nervous")
    team_spirit = input(">What do you suggest Ney should do to spur on the team > ")

    if "motivate" == team_spirit:
        print("The players get hyped and start playing")
        print("It's a penalty for Brazil, Neymar has been tripped in the box")

        print("Neymar steps up to take the penalty,")
        ney_pen = input("> Where should he place it ? >>> ")

        if "up" or "down" in ney_pen:
            print("Neymar scores Brazil take the lead")
            print("GOOOOOOAAAALLLLL, Jubilations around the scenes")
            print("Time is almost up!")
            print("Brazil win 1 - 0")
            WC_won()
        
        if "wide" in ney_pen:
            print("WOW, They couldn't believe that")
            print("Neymar misses from the spot")
            print("Time is almost up")
            wc_final_lost()
            no_balondorwin()
        else:
            print("Sorry couldn't get that!")
            Wc_finals_Half2()
    else:
        print("Try something like motivate....")   
        Wc_finals_Half2()     
#allison part
def allison_saves():
    print("it's the 75th minute")
    print("The opponents striker is through on goal ")
    print("He unleashes his short")
    print("Allisson comes out to save")

    save_dir = input("Where should Allison dive to ? > ")
    if "bottom right" in save_dir:
        print("Allison saves comfortably")
    else:
        print("Allison saves comfortably")  



def GK_saved():
    print("Ouch the keeper saves it.....")        


def WC_won():
    print("And it's all over Brazil are champions")  
    print("Against all odds brazil have won the world cup finals")
    print("Neymar lifts his trophy.....")  
    balon_dor_night()

def WC_won_by1():
    print("Time is almost up.")
    print("Brazil win 1 - 0")
    print("And it's all over Brazil are champions")  
    print("Against all odds brazil have won the world cup finals")
    print("Neymar lifts his trophy.....")  
    balon_dor_night()    

def balon_dor_night():
    print("Neymar arrives in a Rolls Royce")
    print("The ceremony has started")
    balon_dchoice = input("How should Neymar be feeling > ")

    if "nervous" in balon_dchoice:
        print("Neymar shouldn't be")

    elif "relaxed" in balon_dchoice:
        print("Neymar smiles and is confident")

    else: 
        print("I don't quite get that.")   
        balon_dor_night 

    print("Neymar wins the Balon d'or")   
    end()    

def no_balondorwin():
    print("Sorry", username, "You didn't just do enough to help Ney win the Balon dor")
    print("Try again.") 
    end()               

def wc_final_lost():
    print("Head in hands for Neymar and the Seleção Canarinha") 
    print("It was not meant to be this time.")  
    


def ney_determine():
    print("It's a cold morning in South eastern Sao Paulo.")
    print("Neymar really wants to end his career among the greats")
    ney_thoughts = False

    while True:
        ney_time = input("What should Ney do Advice him > ")

        if ney_time == "take it easy":
            print("That wasn't really good")
            no_balondorwin()
        elif ney_time == "work hard" and not ney_thoughts:
            print("Seems like it's starting to come together")
            print("He's now taking everything to thought.")
            ney_thoughts = True
        elif ney_time == "put in work" and ney_thoughts:
            print("Neymar makes up his mind to do what he's supposed to")
            szn_gone_great() 
            #put preceeding funct
        elif ney_time == "train hard" and ney_thoughts:
            print("Neymar makes up his mind to work through everything")
            #put preceeding funct
        else:
            print("That seeems not valid.......")    

def szn_gone_great():
    print(f"""
          Due to the great advice you gave to Neymar he has had a mad season
          scoring 65 and assisting 74 across all competitions and winning all honours
          in Saudi Arabia
          HE GOES TO THE 2026 WORLD CLUB ON A HIGH THANKS TO YOU {username}  
          """)
    Wc_finals_Half1()

def szn_not_gone_great():
    print("""
          Your advice was not really great at all Ney has had a not so good season
          scoring 20 and assisting 15 which was not enough to give him a strong footing 
          High numbers by normal players but not up to standard he ends up winning nothing 
          """)
    no_balondorwin()

def end():
    print("Thanks for helping Ney....., Goodbye")
    exit(0)   


def ney_move():
    print("It's a troubling season for Neymar")
    print("He feels fitter and stronger than ever")  
    print("But...........")
    print("He wishes to crown his career with a Balon'dor ")

    ney_plan = input("> Should he seek advice or party ?")

    if "seek advice" in ney_plan:
        print("That's where you come in")
        print("He tells you to come to him the next week on the same day")
        ney_determine()

    elif "party" in ney_plan:
        print("Ney proceeds to party in Miami the next week") 
        print("was that really smart ?")

    else:
        print("Couldn't quite get that, try again.....")
        ney_move()

ney_move()        