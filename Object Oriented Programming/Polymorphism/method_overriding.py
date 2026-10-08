'''Method Overriding allows a child to provide a specific implementation of a method that is already defined in its parent class.'''

## Base Class
class Animal:
    def speak(self):
        return "Sound of the Animal"

## Derived Class 1
class Dog(Animal):
    def speak(self):
        return "Woof!"

## Derived Class 
class Cat(Animal):
    def speak(self):
        return "Meow!"

## Function that demonstrates polymorphism
def animal_speak(animal):
    print(animal.speak())

Sumo = Dog()
Kitty = Cat()
print(Sumo.speak())
print(Kitty.speak())
animal_speak(Kitty)