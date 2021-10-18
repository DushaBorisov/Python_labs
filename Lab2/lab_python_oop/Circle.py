import math

from lab_python_oop.GeometricShape import GeometricShape
from lab_python_oop.ShapeColour import ShapeColour


class Circle(GeometricShape):

    name = "Circle"

    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = ShapeColour()
        self.colour = colour

    def calculate_square(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        print("Colour: {}, Square: {}".format(self.colour, self.calculate_square()))

    @classmethod
    def get_shape_name(cls):
        print(cls.name)
