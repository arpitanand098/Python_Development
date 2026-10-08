## Base Class
class Shape:
    def area(self):
        return " The area of the figure"

## Derived Class 1
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

## Derived Class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

## Function That demonstrates polymorphism

def print_area(shape):
    print(f"The area is {shape.area()}")

rectangle = Rectangle(4,6)
circle = Circle(6)

print_area(rectangle)
print_area(circle)