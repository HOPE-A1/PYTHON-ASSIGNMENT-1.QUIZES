import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def getCircumference(self):
        return 2 * math.pi * self.radius

c1 = Circle(5)
print("Area:", c1.getArea())
print("Circumference:", c1.getCircumference())
