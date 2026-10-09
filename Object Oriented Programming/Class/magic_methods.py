'''Magic methods are predefined methods in python that you can override to change the behaviour of your objects.'''
class Person:
### Bagic Methods
   def __init__(self,name,age):
       self.name = name
       self.age = age

   def __str__(self):
       return f"{self.name} is {self.age} years old."

   def __repr__(self):
       return f"Person(name = {self.name}, age= {self.age})"

person = Person("Arpit", 20)
print(person)
print(repr(person))

'''Some Common Magic methods include:
    __init__ : Intializes a new instance of class
    __str__: Returns a string representation of an object
    __repr__: Returns an official string representation of an object.
    __len__: Returns the length of an object.
    __getitem__: Gets an item from a container
    __setitem__: Sets an item in a container'''




