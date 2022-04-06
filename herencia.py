class Rectangle:

    def __init__(self, base, heigh):
        self.base = base
        self.heigh = heigh

    def area(self):
        return self.base * self.heigh


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)


if __name__ == '__main__':
    rectangle = Rectangle(base = 3 , heigh = 4)
    print(rectangle.area())

    square = Square(side = 5)
    print(square.area())