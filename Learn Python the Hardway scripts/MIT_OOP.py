#Making and using our own types with classes 

#Code in context of a coordinate object
#we define the class with a name

#                                    |
#                                    |
#                                    |
#                           __________________
#                                    |
#                                    |
#                                    |
#                                    |
#                                    |


#we define a class with by calling forth class and name the type of our class which in this case is coordinate in the parathesis we put the parent of the class 
#which will be named object
class Coordinate(object):
    #attributes here (data and proceedures that belong to the class)
    def __init__(self, x, y):
        self.x = x
        self.y = y

#self is always the instance of the object you're going to perform the operation on 
#other is another parameter to method.........
#dot notation is used to access the data
    def distance(self, other):
        x_diif_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diif_sq + y_diff_sq) **0.5    
    

#self becomes the object variable C
c = Coordinate(3, 4) #create a new object of type Coordinate and pass in 3 and 4 to the __init__
origin = Coordinate(0, 0)
print(c.x)
print(origin.x)
zero = Coordinate(0, 0 )
print(c.distance(zero))

#Methods are are procedural attributes that allow us to interact with our objects 

#special operators in python
#like print, can override these to work with your class

#define them with double underscores before/after
#__add__(self, other)
#__sub__(self, other)
#__str(self)
#self == other
#self < other