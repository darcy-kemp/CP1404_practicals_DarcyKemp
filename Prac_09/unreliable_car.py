from Prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but doesn't drive randomly based on reliability."""
        if self.reliability > random.randint(1, 99):
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
