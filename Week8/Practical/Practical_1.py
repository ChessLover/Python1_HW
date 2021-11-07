# Create the class Animal.
# Attributes: name
# Methods: __init__(self, name) -> creates the attribute name
# move(self) -> prints “I can move”
# Create the class Dog which inherits from the class Animal.
# Attributes: -
# Methods: __init__(self) -> calls the __init__ method of the Animal with a value “Dog”
# Create an object of class Dog and call the method move() from the object.
# Now, add a method move(), which prints “I can run really fast”.
# Create an object of class Dog and call the method move() from the object.


class Animal: 
    def __init__(self, name): 
        self.name = name
    
    def move(self):
        return print("I can move")

class Dog(Animal):    
    def __init__(self): 
        super().__init__("Dog")

    def move(self):
        return print("I can run really fast")


dog1 = Dog()
dog1.move()




