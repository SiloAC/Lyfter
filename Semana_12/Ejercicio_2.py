import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            print("Warning: Radius must be positive. It will be set as 0.")
            self.radius = 0
        else:
            self.radius = radius

    def calculate_perimeter(self):
        if self.radius == 0:
            return 0
        return 2 * math.pi * self.radius

    def calculate_area(self):
        if self.radius == 0:
            return 0
        return math.pi * self.radius ** 2
    
class Square(Shape):
    def __init__(self, side):
        if side <= 0:
            print("Warning: side must be positive. It will be set as 0")
            self.side = 0
        else:
            self.side = side

    def calculate_perimeter(self):
        if self.side == 0:
            return 0
        return 4 * self.side

    def calculate_area(self):
        if self.side == 0:
            return 0
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            print("Warning: The width and height must be positive. They will be set as 0.")
            self.width = 0
            self.height = 0
        else:
            self.width = width
            self.height = height

    def calculate_perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def calculate_area(self):
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * self.height


circle = Circle(-5)
print("Circle - Perimeter:", circle.calculate_perimeter())
print("Circle - Area:", circle.calculate_area())

square = Square(4)
print("Square - Perimeter:", square.calculate_perimeter())
print("Square - Area:", square.calculate_area())

rectangle = Rectangle(3, -6)
print("Rectangle - Perimeter:", rectangle.calculate_perimeter())
print("Rectangle - Area:", rectangle.calculate_area())