import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage
c = Circle(7)

print("Radius:", c.radius)
print("Area of circle:", c.area())
print("Perimeter of circle:", c.perimeter())