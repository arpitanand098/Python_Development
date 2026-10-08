'''Abstract Base Classes (ABCs) are used to define common methods for a group of related objects.They can enforce that derived classes implement particular methods, promoting consistency across different implementations.'''

from abc import ABC, abstractmethod

## Define an Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

## Derived Class
class Car(Vehicle):
    def start_engine(self):
        return "Car Engine Started"

## Derived Class 2
class Bike(Vehicle):
    def start_engine(self):
        return "Bike Engine Started"

## Function that demonstartes Polymorphism

def start_Vehicle(vehicle):
   print(vehicle.start_engine())


## Creating Objects of Car and Bike
BMW = Car()
Royal_Enfield = Bike()
start_Vehicle(BMW)