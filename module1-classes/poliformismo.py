
class Person:

    def __init__(self, name):
        self.name = name

    def moves(self):
        print('Ando caminando')


class Cyclist(Person):

    def __init__(self, name):
        super().__init__(name)

    def moves(self):
        print('Ando moviéndome en mi bicicleta')


def main():
    person = Person('Juan')
    person.moves()

    cyclist = Cyclist('Daniel')
    cyclist.moves()


if __name__ == '__main__':
    main()