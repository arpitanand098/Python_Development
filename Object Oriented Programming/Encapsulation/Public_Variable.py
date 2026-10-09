class Person:
    def __init__(self,name,age):
        self.name = name ## Public Variables
        self.age = age ## Public Variables

def get_name(person):
    return person.name

person = Person("Arpit", 20)
print(get_name(person))
print(person.name)

print(dir(person))

