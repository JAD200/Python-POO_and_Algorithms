# Decoratos
##* This code has been taken from this video: https://bit.ly/3x7EsJ6

def decorator_func(parameter_func):

    def interior_func(*args, **kwargs):
        print(f'\nRealizando calculo. . . \nEl resultado es: ')
        parameter_func(*args, **kwargs)

    return interior_func

@decorator_func
def suma(num1, num2, num3):
    print(num1 + num2 + num3)

@decorator_func
def potencia(base, exponente):
    print(pow(base, exponente))

suma(3, 10, 110)

potencia(base=5, exponente=3)
