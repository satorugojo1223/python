class Vehicle:
    def __init__(self, name, fare, capacity):
        self.name = name
        self.fare = fare
        self.capacity = capacity

    def display(self):
        print("Vehicle:", self.name)
        print("Fare per person:", self.fare)
        print("Capacity:", self.capacity)


class Bus(Vehicle):
    def __init__(self, name, fare, capacity):
        # calling parent constructor
        super().__init__(name, fare, capacity)

    def total_fare(self):
        # adding 10% maintenance charge
        total = self.fare * self.capacity
        maintenance = total * 0.10
        return total + maintenance


# Example usage
bus = Bus("School Bus", 50, 40)

bus.display()
print("Total Bus Fare:", bus.total_fare())