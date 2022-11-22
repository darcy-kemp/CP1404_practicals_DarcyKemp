from Prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):

    def __init(self, name, fuel, fanciness):
        flagfall = 4.50
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
        self.flagfall = flagfall

    def get_fare(self):
        """Return the price for the trip."""
        return super().get_fare() * self.fanciness + self.flagfall

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

    def __str__(self):
        return f"{self.name}, fuel = {self.fuel}, odometer = {self._odometer}, {self.current_fare_distance} on " \
               f"current fare, {(self.fanciness * self.price_per_km):.2f}/km plus flagfall of {self.flagfall} "
