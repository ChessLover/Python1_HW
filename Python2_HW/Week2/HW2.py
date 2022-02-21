# Use prototype design pattern and classes of your choice. create an abstract class Shape and
# concrete classes extending the Shape class: Circle, Square and Rectangle. Define a class
# ShapeCache which stores shape objects in a dictionary and returns their clones when
# requested. Create some objects and do some operations to test your classes.

# ---------------------------------------------------------------------------------------

from abc import ABCMeta, abstractmethod
import copy


class Shape(metaclass = ABCMeta): 
    
    def __init__(self): 
        self.color = None
        self.shape_type = None
    
    @abstractmethod
    def shape(self): 
        pass

    def get_shape_type(self):
        return self.shape_type
            
    def set_color(self, shape_color):
        self.color = shape_color

    def get_color(self):
        return self.color

    def clone(self):
        return copy.copy(self)


class Circle(Shape): 
    
    def __init__(self): 
        super().__init__()
        self.shape_type = "circle"
        
        
    def shape(self): 
        print("I am the circle one!")
    
class Square(Shape): 
    
    def __init__(self): 
        super().__init__()  
        self.shape_type = "square"
        
    def shape(self): 
        print("I am the square one!")

class Rectangle(Shape): 
    
    def __init__(self): 
        super().__init__()
        self.shape_type = "rectangle"
    
    def shape(self): 
        print("I am the rectangle one!")
    


class ShapeCache: 
    
    cache = {}

    @staticmethod
    def get_shape(cid): 
        
        shape_cache = ShapeCache.cache.get(cid, None)
        #creates an exact copy of COURSE, we copy so that the manipulations won't affect 
        #the original cached object
        return shape_cache.clone() 
        
    
    @staticmethod
    def load(): 
        
        c = Circle()
        c.set_color("red")
        ShapeCache.cache[c.get_color()] = c
  
        s = Square()
        s.set_color("green")
        ShapeCache.cache[s.get_color()] = s
  
        rect = Rectangle()
        rect.set_color("blue")
        ShapeCache.cache[rect.get_color()] = rect



# ---------------------------------------------------------------------------------------

ShapeCache.load()

print("*******************")

circ = ShapeCache.get_shape("red")
print(circ.get_shape_type())
print(circ.get_color())

print("*******************")

sqr = ShapeCache.get_shape("green")
print(sqr.get_shape_type())
print(sqr.get_color())

print("*******************")

rec = ShapeCache.get_shape("blue")
print(rec.get_shape_type())
print(rec.get_color())

print("*******************")

triangle = ShapeCache.get_shape("red")
triangle.color = "yellow"
triangle.shape_type = "triangle"
print(triangle.get_color())
print(triangle.get_shape_type())

print("*******************")











