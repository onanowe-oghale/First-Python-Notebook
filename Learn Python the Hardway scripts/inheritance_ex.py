# inheritance exercise

class Dog:

    species = "Canis Familiaris"

    def __init__ (self, name , age):
        self.name = name
        self.age = age
    
    def str(self):
        return f"This is {self.name} and he is {self.age}"
    
    def speak (self , sound):
        return f"This is the dog {self.name} and it makes the sound {sound}"

class GoldenRetriever(Dog):
    def speak (self, sound = "Ouch ouch"):
        return super().speak(sound)
    
sul = GoldenRetriever("Sully", 5)

print(sul.speak())

print(isinstance(GoldenRetriever, Dog))