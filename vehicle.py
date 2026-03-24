class BMW:
    def fuel_type(self):
        return "BMW uses Petrol/Diesel"

    def max_speed(self):
        return "BMW max speed is 250 km/h"


class Ferrari:
    def fuel_type(self):
        return "Ferrari uses Petrol"

    def max_speed(self):
        return "Ferrari max speed is 340 km/h"


# Polymorphism in action
cars = [BMW(), Ferrari()]

for car in cars:
    print(car.fuel_type())
    print(car.max_speed())
    print("-----")