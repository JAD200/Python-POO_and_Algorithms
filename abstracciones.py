
class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura = 'caliente'):
        print(f'\nIniciando . . .')
        self._llendar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llendar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print('Añadiendo jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa\n')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()