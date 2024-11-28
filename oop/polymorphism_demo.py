import math

# Base Class - Shape
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Area of rectangle = length * width
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Area of circle = π * radius^2
        return math.pi * self.radius ** 2
