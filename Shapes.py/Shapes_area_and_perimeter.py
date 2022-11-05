# importing the ABC module, inorder to use the Abstract classes and Methods
from abc import ABC, abstractmethod
# abstract class Shapes
class Shapes(ABC):
#     Abstact method for area
    @abstractmethod
    def area(self):
        pass
#    abstract method for Perimeter
    @abstractmethod
    def perimeter(self):
        pass
# subclass Square 
class Square(Shapes):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4*self.side
# subclass Rectangle 
class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length*self.width
    
    def perimeter(self):
        return 2*(self.length+self.width)
# Subclass Circle
class Cicle(Shapes):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius
# Subclass Triangle   
class Triangle(Shapes):
    def __init__(self, base, height):
        self.height=height
        self.base=base
        
    def area(self):
        return 0.5*self.base*self.height
    def perimeter(self):
        return 3*self.base
    

        


    
