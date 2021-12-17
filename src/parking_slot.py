class ParkingSlot(object):
    """
    ParkingSlot class has attribute of parking slot.
    """

    def __init__(self, slot_number=None, is_available=False):
        # this car is parking specific number
        self.car = None
        self.slot_number = slot_number
        self.is_available = is_available

    def car(self, value):
        self.car = value

    def slot_number(self, value):
        self.slot_number = value

    def is_available(self, value):
        self.is_available = value
