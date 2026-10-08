## When a class inherits from more than one base class.
# Base class 1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Subclass must implement this method")

## Base class 2
class Pet:
    def __init__(self, owner):
        self.owner = owner

## Derived Class
class Dog(Animal, Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self, owner)

    def speak(self):
        return f"{self.name} say woof"


## Create an object
dog = Dog("Max", "Arpit")
print(dog.speak())
print(f"Name: {dog.name}")
print(f"Owner: {dog.owner}")

