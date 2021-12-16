class ParkingSlot(object):
    """
    ParkingSlot class has attribute of parking slot.
    """

    def __init__(self, slot_number=None, is_available=False):
        # this car is parking specific number
        self.car = None
        self.slot_number = slot_number
        self._is_available = is_available

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, value):
        self._car = value

    @property
    def slot_number(self):
        return self._slot_number

    @slot_number.setter
    def slot_number(self, value):
        self._slot_number = value

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, value):
        self._is_available = value
