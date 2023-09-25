# players class creation 

class Players:
    player_club = "Manchester United"
    def __init__(self, age , name):
        self.age = age
        self.name = name

Rashford = Players (22 , "Rashford")

print(Rashford.name)