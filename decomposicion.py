
class Car:
    """ class Car
    Constructor
        model = model
        brand = brand
        color = color
        _state = 'en_reposo'
        _engine = class Engine
        _wheels = class Wheels

    """
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._state = 'en_reposo'
        self._engine = Engine(cylinders=4, engine_type='gasolina')
        self._wheels = Wheels(35, 'non-skid', 'Michelin')

    def accelerate(self, type='slow'):
        """ Simulation of a car accelerating and decelerating.

        Args:
            type (str, optional): Defines the speed which the car accelerates. Defaults to 'slow'.

        """
        if type == 'fast':
            self._engine.fuel_injection(20)
            self._wheels.wheels_use(2)
        else:
            self._engine.fuel_injection(7)
            self._wheels.wheels_use(1)

        self._state = 'en_movimiento'


class Engine:
    """ class Engine
    Constructor
        cylinders = cylinders
        engine_type = engine_type
        fuel_level = fuel_level
        _temperature = 0

    """
    def __init__(self, cylinders, engine_type, fuel_level=1000):
        self.cylinders = cylinders
        self.engine_type = engine_type
        self.fuel_level = fuel_level
        self._temperature = 0

    def fuel_injection(self, quantity):
        """ Simulates the injection of fuel to an engine and
        also defines the temperature of it.

        Args:
            quantity (int): Quantity of fuel injected to the engine
        """
        self.fuel_level -= quantity
        if quantity >= 10:
            self._temperature = 110
        else:
            self._temperature = 80


class Wheels:
    """ class Wheels
    Constructor
        tread_width = tread_width
        type = type
        brand = brand
        _temperature = 0
        _state = 'filled'

    """
    def __init__(self, tread_width, type, brand):
        self.tread_width = tread_width
        self.type = type
        self.brand = brand
        self._temperature = 0
        self._state = 'filled'

    def wheels_use(self, use_state):
        """ Simulation of the wheels warming when the car accelerates

        Args:
            use_state (int): state of the wheels
        """
        if use_state == 1:
            self._temperature = 90
        elif use_state == 2:
            self._temperature = 125


if __name__ == "__main__":
    car1 = Car("AAFF","toyota", "rojo")
    car1.accelerate('slow')
    car1.accelerate('fast')