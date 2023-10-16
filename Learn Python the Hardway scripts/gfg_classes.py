#a class with a method m that prints in class 1
class class1:
    def m(self):
        print("In class 1")

#inherits from class1 and overrides the method m to print additinal messages
#They also super().m() to invoke methods of the base class (class 1)
class class2(class1):
    def m (self):
        print("In class 2")
        super().m()

#inherits from class 1 and overrides the methods m to print additional messages
#it also uses the super().m() to invoke methods of the base class(class 1)
class class3(class1):
    def m(self):
        print("In class 3")
        super().m()

#class 4 inherits from class2 and class3 and the m method is overwritten to print a different string
#it class the super().m() to invoke the methods of its base classes (class2 and class3)
class class4(class2, class3):
    def m (self):
        print("In class 4")
        super().m()

#prints the MRO as list.
#The method MRO is the order in which python looks methods in class hierarchy
print(class4.mro())

#this prints the MRO as a tuple.
print(class4.__mro__)



#super function is used to give access to methods and properties of a parent or sibiling class.
#the super function returns an object that represents the parent class
