class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def describe(self):
        print(f"The {self.name} moves at a speed of {self.speed} km/h.")

# Child class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, name, speed, fuel_type):
        super().__init__(name, speed)  # Calling the __init__ method of the Vehicle class
        self.fuel_type = fuel_type  # Additional attribute unique to Car

    def describe(self):
        # Overriding the describe method to include fuel_type
        super().describe()  # Call the describe method from Vehicle class
        print(f"It runs on {self.fuel_type}.")

# Another child class inheriting from Vehicle
class Bicycle(Vehicle):
    def __init__(self, name, speed, gear_count):
        super().__init__(name, speed)
        self.gear_count = gear_count  # Additional attribute unique to Bicycle

    def describe(self):
        # Overriding the describe method to include gear_count
        super().describe()
        print(f"It has {self.gear_count} gears.")

# Creating objects from our classes
my_car = Car("Toyota", 120, "petrol")
my_bicycle = Bicycle("Mountain Bike", 30, 21)

# Using the objects
my_car.describe()
my_bicycle.describe()
