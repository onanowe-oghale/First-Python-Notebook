mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

import mystuff
mystuff.apple

print(mystuff.tangerine)


# mystuff['apple'] #get apple from dict
# mystuff.apple() # gets apple from the module
# mystuff.tangerine #same thing , it's just a variable

class Mystuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

#------------------------------------------------------------------------------------------------------------------------------------------------
#objects 

thing = Mystuff()
thing.apple()
print(thing.tangerine)  

#--------------------Getting things from things--------------------
#dict style
mystuff['apples']

#module style
mystuff.apples()
print(mystuff.tangerine)

#class style
thing = Mystuff()
thing.apples()
print(thing.tangerine)

#--------------------A first class-------------------------------------------