''' Protected Variables : We can accesess it from derived class but not use it from outside of the class'''
class Person:
    def __init__(self,name,age,gender):
        self._name = name ## Protected Variables
        self._age = age ## Protected Variables
        self.gender = gender

class Employee(Person):
        def __init__(self, name, age, gender, salary):
            super().__init__(name, age, gender)
            self.salary = salary
            
            
employee = Employee("Arpit", 21, "Male", 10000)
print(employee._name)
print(employee.salary)