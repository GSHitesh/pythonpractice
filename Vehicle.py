class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.fuel_capacity = 20
        self.fuel_level = 0
    
    def start_engine(self):     #We can pass the base class object in the child class
        print("Engine started.")

    def stop_engine(self):
        print(f"Engine of {self.brand} stopped.")

    def __str__(self) -> str:
        return (f"Car is {self.brand} and color is {self.color}")
    
    def add_fuel(self, fuel):
        if self.fuel_level + fuel <= self.fuel_capacity:
            self.fuel_level = fuel + self.fuel_level
            print(f"Current Fuel capacity is {self.fuel_level} out of {self.fuel_capacity} capacity.")
        else:
            print("Tank is already fulled.")
    
class Car(Vehicle):
    def __init__(self, brand, color, num_doors):
        super().__init__(brand,color)
        self.brand = brand
        self.color = color

    
    
    def honk(self):
        super().stop_engine()
        print("Honk! Honk!")

    def add_fuel(self, fuel):
        print("This car has no fuel tank")

    def __str__(self) -> str:
        return super().__str__()    # To call the constructor of base class

class Motorcycle(Vehicle):
    def __init__(self, powercc,vehicle):
        self.power = powercc
        self.vehicle = vehicle

    def start(self):
        self.vehicle.start_engine()

    def wheelie(self):
        super().stop_engine()
        print("Doing a wheelie!")


