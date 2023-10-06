#this is a class named song and it inherits from the base class in the paranthesis called object
class Song(object):
    
#the constructor method __init__ for the song class, it takes two parameters
#time which refers to the instance of the class 
#line it initializes an attribute time.line with the value of line
    def __init__(time, line):
        time.line = line

#this is a method named sing_me_a_song defined with the song class
#it takes time as a parameter referring to the instance of the class
    def sing_me_a_song(time):  
#It iterates over each line in the time.line attributes and prints each line           
        for line in time.line:
            print(line)


#An instance of the song class named happy_bday is created, it is initialized with a list of lyrics 
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there."])    

#This is another instance of the song class named bulls_on_parade is created. It is initialzed with lyrics of the song of the song in the list
bulls_on_parade = Song(["They rally aroung the family",
                        "With pockets full of shells."])  

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()