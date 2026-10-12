'''Operator Overloading allows us to define the behaviour of operators(+, -, *, etc) for custom objects.'''
## Mathematical Operation for vector
class Vector:
     def __init__(self, x, y):
          self.x = x
          self.y = y

     def __add__(self,other):
          return Vector(self.x + other.x, self.y + other.y)

     def __sub__(self,other):
          return Vector(self.x - other.x, self.y - other.y)

     def __mul__(self,other):
          return Vector(self.x * other, self.y * other)
     
     def __eq__(self,other):
          return self.x == other.x, self.y == other.y

     def __repr__(self):
          return f"Vector({self.x}, {self.y})"

## Create objects of the Vector  Class
v1 = Vector(5, 9)
v2 = Vector(6, 8)

print(v1 + v2)
print(v1-v2)
print(v1 * 5)

## Overloading Operators for complex number