class Animal(object):
    pass

#is a 
class Dog(Animal):

    def __init__(self, name):
        #has a
        self.name = name

# is a
class Cat(Animal):

    def __init__(self, name):
        #has a 
        self.name = name

#is a 
class person(object):

    def __init__(self, name,):
        #has a 
        self.name = name        
        
        #person has a pet of some kind
        self.pet = None

class Employee(person):

    def __init__(self, name, salary):
        
