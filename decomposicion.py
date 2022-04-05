
class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._state = 'en_reposo'
        self._engine = Engine(cylinders=4, engine_type='gasolina')
        self._wheels = Wheels(35, 'non-skid', 'Michelin')

    def accelerate(self, type='slow'):
        if type == 'fast':
            self._engine.fuel_injection(20)
            self._wheels.wheels_use(2)
        else:
            self._engine.fuel_injection(7)
            self._wheels.wheels_use(1)

        self._state = 'en_movimiento'


class Engine:

    def __init__(self, cylinders, engine_type, fuel_level=1000):
        self.cylinders = cylinders
        self.engine_type = engine_type
        self._temperature = 0
        self.fuel_level = fuel_level

    def fuel_injection(self, quantity):
        self.fuel_level -= quantity
        if quantity >= 10:
            self._temperature = 110
        else:
            self._temperature = 80


class Wheels:

    def __init__(self, tread_width, type, brand):
        self.tread_width = tread_width
        self.type = type
        self.brand = brand
        self._temperature = 0
        self._state = 'filled'

    def wheels_use(self, use_state):
        if use_state == 1:
            self._temperature = 90
        elif use_state == 2:
            self._temperature = 125


if __name__ == "__main__":
    car1 = Car("AAFF","toyota", "rojo")
    car1.accelerate('slow')
    car1.accelerate('fast')