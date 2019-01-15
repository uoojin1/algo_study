''' How would u design a parking lot?
using oop
''' 

class Vehicle:
    def __init__(self, plateNumber, size):
        self.plateNumber = plateNumber
        self.size = size

class Car(Vehicle):
    def __init__(self, plateNumber, size):
        Vehicle.__init__(self, plateNumber, 1)

class Bus(Vehicle):
    def __init__(self, plateNumber, size):
        Vehicle.__init__(self, plateNumber, 8)
        
class MotorCycle(Vehicle):
    def __init__(self, plateNumber, size):
        Vehicle.__init__(self, plateNumber, 0.5)

class ParkingSpace:
    def __init__(self, location):
        self.empty = True
        self.location = location

class ParkingFloor:
    def __init__(self, level):
        

class ParkingLot:
    def __init__(self, levels):
        self.levels = levels
        self.
