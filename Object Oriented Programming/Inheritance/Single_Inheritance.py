
class Car:
    def __init__(self, brand, price, year, engine_type):
        self.brand = brand
        self.price = price
        self.year = year
        self.engine_type = engine_type

    def drive(self):
        print(f"The person will drive the {self.brand} car.")

car1 = Car("BMW", 80000, 2025, "petrol")
car1.drive()

class BMW(Car):
    def __init__(self, brand, price, year, engine_type, is_selfdriving):
        super().__init__(brand, price, year, engine_type)
        self.is_selfdriving = is_selfdriving
    def selfdriving(self):
        print(f"BMW supports self driving: {self.is_selfdriving}")

BMW1 = BMW("BMW", 100000, 2025, "diesel", True)
BMW1.selfdriving()

BMW1.drive()

