class ShapeColour:
    def __init__(self):
        self.__colour = ""

    def set_colour(self, colour):
        self.__colour = colour

    def get_colour(self):
        return self.__colour

    colour_settings = property(get_colour, set_colour)
