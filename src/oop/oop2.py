# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.


class GroundVehicle():
    def __init__(self, num_wheels):
        self.num_wheels = num_wheels or 4

    def drive(self):
        return 'vroooom'


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels):
        super().__init__(num_wheels)

    def drive(self):
        return 'BRAAAP!!'


vehicles = [
    GroundVehicle(2),
    GroundVehicle(2),
    Motorcycle(2),
    GroundVehicle(2),
    Motorcycle(2),
]

# Go through the vehicles list and print the result of calling drive() on each.

for x in vehicles:
    print(x.drive())
