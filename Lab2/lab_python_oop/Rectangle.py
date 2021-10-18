from lab_python_oop.GeometricShape import GeometricShape
from lab_python_oop.ShapeColour import ShapeColour


class Rectangle(GeometricShape):
    name = "Rectangle"

    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = ShapeColour()
        self.colour = colour

    def calculate_square(self):
        return self.height * self.width

    def __repr__(self):
        print("Colour: {}, Square: {}".format(self.colour, self.calculate_square()))

    @classmethod
    def get_shape_name(cls):
        print(cls.name)
