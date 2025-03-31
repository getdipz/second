import math

# Base class Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius  # radius of the circle

    def getArea(self):
        # Area of the circle: π * r^2
        return math.pi * self.radius ** 2

# Derived class Cylinder (inherits from Circle)
class Cylinder(Circle):
    def __init__(self, radius, height):
        # Call the constructor of the base class
        super().__init__(radius)
        self.height = height  # height of the cylinder

    # Overriding getArea method to calculate the surface area of the cylinder
    def getArea(self):
        # Surface area of the cylinder: 2 * π * r * (r + h)
        return 2 * math.pi * self.radius * (self.radius + self.height)

    # Method to calculate the volume of the cylinder
    def getVolume(self):
        # Volume of the cylinder: π * r^2 * h
        return math.pi * self.radius ** 2 * self.height

# Create an object for the Cylinder class
cylinder = Cylinder(5, 10)  # radius = 5, height = 10

# Output the area of the cylinder (overridden method)
print(f"Surface Area of the Cylinder: {cylinder.getArea():.2f} square units")

# Output the volume of the cylinder
print(f"Volume of the Cylinder: {cylinder.getVolume():.2f} cubic units")
