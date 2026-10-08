class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
      print(f"{self.name} says Woof")

dog1 = Dog("Sumo", 3)
dog1.bark()

dog2 = Dog("Max", 6)
dog2.bark()