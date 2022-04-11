
class Lavadora:
    """ class Lavadora
    This is just a fake class to understand the concept of abstractions
    and private parameters
    """
    def __init__(self):
        pass


    def lavar(self, temperatura = 'caliente'):
        # All these parameters are private because user isn't interested in all those details
        print(f'\nIniciando . . .')

        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

        print(f'\t* * Finalizado * *\n')

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')


    def _anadir_jabon(self):
        print('Añadiendo jabón')

    def _lavar(self):
        print('Lavando la ropa')


    def _centrifugar(self):
        print('Centrifugando la ropa')



if __name__ == '__main__':

    lavadora = Lavadora()
    lavadora.lavar()