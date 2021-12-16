class Car(object):
    """
    Car class has attribute of car.
    """

    def __init__(self):
        self._registration_number = None
        self._colour = None

    @property
    def registration_number(self):
        return self._registration_number

    @registration_number.setter
    def registration_number(self, value):
        self._registration_number = value

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        self._colour = value

    @classmethod
    def create(cls, registration_number, colour):
        car_object = cls()
        car_object.registration_number = registration_number
        car_object.colour = colour
        return car_object