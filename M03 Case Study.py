"""
@author: Kevin Ambler
@file: vehicle_info.py
@desc: Accepts vehicle type, then accepts additional info is vehicle is a car, then outputs user input in formatted way
"""

class Vehicle():  # Defines the Vehicle superclass
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

class Automobile(Vehicle): # Defines the Automobile class, taking Vehicle as its parent class
    def __init__(self, vehicleType):
        super().__init__(vehicleType)
        # Gets user input for all attributes of Automobile not inherited from Vehicle
        self.year = input("What year of car is this? ")
        self.make = input("What make of car is this? ")
        self.model = input("What model of car is this? ")
        self.doors = input("How many doors does this car have? ")
        self.roof = input("What kind of roof does this car have? ")

vehicle1Type = Vehicle(input("What type of vehicle is this? ")) # Creates an instance of Vehicle
vehicle1 = Automobile(vehicle1Type.vehicleType) # Creates instance of Automobile, taking vehicleType attribute from earlier Vehicle class instance

# Outputs stored attribute information
print("Vehicle Type: ",vehicle1.vehicleType)
print("Year: ",vehicle1.year)
print("Make: ",vehicle1.make)
print("Model: ",vehicle1.model)
print("Number of Doors: ",vehicle1.doors)
print("Type of Roof: ",vehicle1.roof)