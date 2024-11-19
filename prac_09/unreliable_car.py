import random
from prac_09.car import Car

class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability, which affects its ability to drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability  # Set the reliability percentage

    def drive(self, distance):
        """Drive like the Car but only if the random reliability check passes."""
        if random.uniform(0, 100) < self.reliability:
            # If the random number is within reliability, drive the requested distance
            return super().drive(distance)
        else:
            # If the car is unreliable this time, drive 0 km
            return 0
