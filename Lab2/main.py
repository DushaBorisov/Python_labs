from lab_python_oop.Circle import Circle
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Square import Square


def main():

    object1 = Rectangle(5, 5, "blue")
    object1.__repr__()

    object2 = Circle(5, "green")
    object2.__repr__()

    object2 = Square(5, "green")
    object2.__repr__()



if __name__ == "__main__":
    main()