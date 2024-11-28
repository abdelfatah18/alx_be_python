import math

class Shape:
    def area(self):
        raise NotImplementedError("NotImplementedError: Subclass must implement this method.")

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2

# Example usage:
rectangle = Rectangle(10, 20)
print("Rectangle area:", rectangle.area())

circle = Circle(7)
print("Circle area:", circle.area())
