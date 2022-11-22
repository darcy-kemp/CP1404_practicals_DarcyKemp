from Prac_09.unreliable_car import UnreliableCar

car0 = UnreliableCar("Holden", 1000, 25)
car1 = UnreliableCar("Mitsubishi", 1000, 50)
car2 = UnreliableCar("Prius", 1000, 75)


for i in range(0, 4, 1):
    print(car0.drive(50))
    print(car1.drive(50))
    print(car2.drive(50))