class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def describe(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def describe(self):
        return f"Car: {super().describe()}"

class Motorcycle(Vehicle):
    def describe(self):
        return f"Motorcycle: {super().describe()}"

car = Car("Toyota", "Camry", 2020)
moto = Motorcycle("Harley", "Davidson", 2019)

print(car.describe())
print(moto.describe())
