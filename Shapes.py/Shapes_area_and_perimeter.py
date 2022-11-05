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
    
# Choice of shape and input of values  
def Choice():
    print("Area and Perimeter of the shapes Calculator")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        print(f"Your choice is {choice}.")
        side = int(input("Enter the side of the square: "))
        square = Square(side)
        print("Area of the square: ", square.area())
        print("Perimeter of the square: ", square.perimeter())
        
    elif choice==2:
        print(f"Your choice is {choice}.")
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        rectangle = Rectangle(length, width)
        print(f"Area of the rectangle: {rectangle.area()} cm")
        print(f"Perimeter of the rectangle: {rectangle.perimeter()} cm")
        
    elif choice==3:
        print(f"Your choice is {choice}.")
        radius=int(input("Enter the radius of the circle: "))
        circle=Cicle(radius)
        print("Area of the circle: ", circle.area())
        print("Perimeter of the circle: ", circle.perimeter())
        
    elif choice==4:
        print(f"Your choice is {choice}.")
        height=int(input("Enter the height of the Triangle: "))
        base=int(input("Enter the base of the Triangle: "))
        triangle=Triangle(height,base)
        print("Area of the circle: ", triangle.area())
        print("Perimeter of the circle: ", triangle.perimeter())
        
    elif choice==5:
        exit()
       
    else:
        print("Invalid Choice")
        


    
