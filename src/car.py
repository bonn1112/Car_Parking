class Car(object):
    """
    Car class has attribute of car.
    """

    def __init__(self):
        self.registration_number = None
        self.colour = None

    def registration_number(self, value):
        self.registration_number = value

    def colour(self, value):
        self.colour = value

    @classmethod
    def create(cls, registration_number, colour):
        car_object = cls()
        car_object.registration_number = registration_number
        car_object.colour = colour
        return car_object
