#animal is a objec
class Animal(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print("We Run")

#Dog is a animal
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

#is employee is a person
class Employee(person):

    def __init__(self, name, salary):
        
        super(Employee, self).__init__(name)

        self.salary = salary 

#is a 
class Fish(object):
    
    def __init__(self, name):
        self.name = name

    def swim (self):
        print(f"{self.name} swims fast")    

#is a - This a class that is a subclass of fish 
class salmon(Fish):
    pass

#is a - this is a class that isa subclass of fish
class Halibut(Fish):
    pass

## rover is- a Dog
rover  = Dog("Rover")

#santan is a cat
santan = Cat("Santan")

#mary is a person
mary = person("Mary")

#has
#mary has a pet named santan
# class dog gets into class pet - santan from the dog class gets into class person with the pet 
mary.pet = santan

#frank is an instance of class employee having name frank and salary of 1200000
#frank is an employee
frank = Employee("Frank", 120000)

#frank an employee, has a pet rover
frank.pet = rover

# is a  - as flipper is a instance of class Fish
flipper = Fish('flipper')

# crouse is a - as crouse is a instance of class salmon
crouse = salmon('crouse')

# is a - as harry is a instance of class Halibut
harry = Halibut('harry')

rover.run() #this inherits the run function from dog class which is inherited from the animal class.

oscar = Fish('oscar')

oscar.swim()
crouse.swim()


#is relationships are represented by inheritance which are Dog is an Animal, Employee is a person, salmon is a fish.
#has a relationhips are reprensented by composition like how mary has a pet, frank is a pet.