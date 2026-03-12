class vehicle :
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class bus(vehicle):
    pass

bus1 = bus("school volvo","120km/hr","13km/leter")

print("the name of the bus is",bus1.name)
print("the maxspeed of the bus is",bus1.maxspeed)
print("the mileage of the bus is",bus1.mileage)
