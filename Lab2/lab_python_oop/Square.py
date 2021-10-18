from lab_python_oop.Rectangle import Rectangle


class Square(Rectangle):

    name = "Square"

    def __init__(self, side, colour):
        super().__init__(side, side, colour)

    def __repr__(self):
        print("Colour: {}, Square: {}".format(self.colour, self.calculate_square()))

    @classmethod
    def get_shape_name(cls):
        print(cls.name)
