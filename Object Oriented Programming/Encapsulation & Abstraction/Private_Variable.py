'''Private Variable: Nothing should be accessible Outside of the class'''
class Person:
    def __init__(self,name,age,gender):
        self.__name = name ## Private  Variables
        self.__age = age ## Private Variables
        self.gender = gender ##Public Variables

def get_name(person):
    return person.__name

person = Person("Arpit", 21, "Male")
print(dir(person))
print(get_name(person))