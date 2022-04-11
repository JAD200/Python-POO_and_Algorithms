class Rectangle:
    """ superclass Rectangle
    Constructor
        base = base
        height = height

    """
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        """ Calculates the area of a rectangle
        Args:
            base :int
            heigh :int

        Returns:
            self.base * self.height :int
        """
        return self.base * self.height


class Square(Rectangle):
    """ subclass Square extends superclass Rectangle
    Constructor
        side = base
        side = height

    """
    def __init__(self, side):
        super().__init__(side, side)


if __name__ == '__main__':
    rectangle = Rectangle(base = 3 , height = 4)
    print(rectangle.area())

    square = Square(side = 5)
    print(square.area())