class Person:
    def __init__(self, name, age):
        self.__name = name ## Private Variable or access modifiers
        self.__age = age ## Private Variable

    ## getter method for name
    def get_name(self):
        return self.__name

    ## setter method for name
    def set_name(self, name):
        self.__name = name

    ## getter method for age
    def get_age(self):
        return self.__age

    ## Setter method for age 
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative")


person = Person("Arpit", 21)

##Access and modify private variable using getter and setter
print(person.get_name())
print(person.get_age())

person.set_age(20)
print(person.get_age())

person.set_name("Shristy")
print(person.get_name())