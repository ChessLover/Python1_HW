# Use Factory Method pattern to create 3 different classes Circle, Square and Triangle of type
# Shape having a method Draw with some implementation of your choice. Have a ShapeFactory
# class and a Client class and allow the Client to ask the factory to create some concrete shape
# and to call its method Draw. You can decide what should be the client input and how the factory
# class should determine which shape to create.

# ---------------------------------------------------------------------------------------

class Circle: 
    def __init__(self):
        self.shape = "Circle"

    def Draw(): 
        return print("Great choice! Let's draw a circle.")


class Square: 
    def __init__(self):
        self.shape = "Square"

    def Draw(): 
        return print("Great choice! Let's draw a square.")

    
class Triangle: 
    def __init__(self):
        self.shape = "Triangle"

    def Draw(): 
        return print("Great choice! Let's draw a triangle.")
    
# ---------------------------------------------------------------------------------------

class ShapeFactory: 
    
    def __init__(self):
        self.shape = input("What type of shape you want to draw? : ")
        
    
class Client(ShapeFactory): 

    def __init__(self):
        ShapeFactory.__init__(self)

    def draw_shape(self): 
        
        if self.shape == "Circle": 
            return Circle.Draw()
        elif self.shape == "Square": 
            return Square.Draw()
        elif self.shape == "Triangle": 
            return Triangle.Draw()
        else: 
            return print("Please specify Square, Circle or Triangle.")
        


# ---------------------------------------------------------------------------------------  

cl = Client()
cl.draw_shape()