# Create the class Animal.
# Attributes: name, legs (the number of legs)
# Methods: __init__(self, name, legs) -> creates the attributes name and legs
# getName(self) -> prints “My name is X”, using the value of the attribute name instead of X.
# getLegs(self) -> prints “I have X legs”, using the value of the attribute legs instead of X.
# Create the class Exnik which inherits from the class Animal
# Attributes: -
# Methods: __init__(self) -> calls the __init__ method of the Animal class with a value “Exnik”
# Create an object of class Exnik and call the methods getLegs() and getName() from the object.

class Animal: 
    def __init__(self, name, legs): 
        self.name = name
        self.legs = legs
    
    def getName(self):
        return print("My name is:" , self.name)

    def getLegs(self): 
        return print("I have %d legs." %self.legs)

class Exnik(Animal):    
    def __init__(self): 
        super().__init__("Exnik", 4)



exnik = Exnik()
exnik.getName()
exnik.getLegs()
