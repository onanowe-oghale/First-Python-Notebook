#creating a python class

class song_line_each(object):

    def __init__(self, lines):
        self.line = lines

    def each_line(self):
        for line in self.line:
            print(line)    

ManchesterU = song_line_each(["Glory Glory Manchester united",
                              "Glory Glory Manchester united",
                              "As the reds go marching on\n"])

RealMad = song_line_each(["Madrid, Madrid, Madrid",
                           "¡Hala Madrid!",
                            "Y nada más",
                            "¡Hala Madrid!\n"])  

print("This is going to be three lines from Manchester uniteds anthem")
ManchesterU.each_line()

print("This is going to be three lines from Madrid's Anthem")
RealMad.each_line()
