class song(object):
    
    def __init__(self, lyrics):
        self.line = lyrics

    def line_each(self):
        for line in self.line:
            print(line) 

calledout = song(["That's why all the earth will shout your name",
                  "Our hearts will cry these bones will sing",
                  "Great are you Lord!"])  

calledout2 = song({"RCCG": "Canada",
                   "LONDON":"AWE"})

calledout.line_each()

calledout2.line_each()