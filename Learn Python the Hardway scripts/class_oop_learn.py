#dog.py

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a very good dog for his age {self.age}"

    def color (self, color):
        return f"{self.name} has a color {color}"

    def trip_guess (self, color , height):
        return f" Just at age {self.age} , {self.name} is {height} ft tall and is color {color}"


milly = Dog("milly", 99, "Bulldog")
gerrad = Dog("gerrad", 46, "Russell Terrier")
clamx = Dog("Clamx", 47, "Dachshund")

print(milly.species)
print(clamx.species)

print("We printed their species now their names")

print("Dog 1 is named", milly.name, "And is aged", milly.age)
print("Dog 2 is named", gerrad.name, "Ang is aged", gerrad.age)

"""print(gerrad.decider())
print(gerrad.color("blue"))
print(gerrad.trip_guess("brown", "5t 9in"))"""

print(gerrad.color ("gREEN"))
print(milly.color ("Yellow"))

names = ["milly", "gerrad", "clamx"]
print (names)
print(milly)

print(milly.breed)

#Class 2-----------------------------------
class Ball:
    def __init__(self, material , speed):
        self.material = material
        self.speed = speed

    def __str__(self):
        return f"The balls is ,made of {self.material} and moves at a speed of {self.speed} KM/H" 


brazuka = Ball("Leather" , 4000)
javulani = Ball("Pig Skin" , 5500)

for Ball in (brazuka , javulani):
    print(Ball)