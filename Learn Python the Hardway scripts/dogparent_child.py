# dogparent_child.py

class Dog:
    specie = "Canis Familiaris"

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def sound(self, sound):
        return f"{self.name} makes the sound {sound}"  

"""miles = Dog("miles", 4)
buddy = Dog("Buddy", 5)
jack = Dog("Jack", 3)

print(miles.age)

print(miles.sound("ouch ouch"))
print(jack)"""

class JackRussellTerrier(Dog):
    def speak(self, sound = "Arf"):
        return super().sound(sound)
class Dachsund(Dog):
    def speak(self ,sound = "ARGh argh argh"):
        return f"{self.name} barks {sound}"
class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachsund("Buddy", 9)
jack = JackRussellTerrier("Jack", 3)

print(buddy.name)
print(jack.name)

print(jack.sound("ouch ouch"))

print(type(miles))

print(isinstance(miles, Dog))
print(isinstance(buddy, Dachsund))

print(miles.speak())
print(miles.speak("Grrrrr"))

print(buddy.speak("Up up up"))