from Car_Parking.src import car, parking_slot


class Parking(object):
    """
    Parking class which has details about parking slots
    as well as operation performed on parking are present here
    """

    def __init__(self):
        self.slots = {}

    def create_parking_lot(self, number_of_slots):
        """create parking lot
        :param number_of_slots - Integer
        """

        if self.slots is not None:
            print("Parking lot is already created")

        number_of_slots = int(number_of_slots)

        # update slots and availability
        if number_of_slots > 0:
            for i in range(1, number_of_slots + 1):
                self.slots[i] = parking_slot.ParkingSlot(slot_number=i,
                                                         is_available=True)
            print("Created a parking lot with %s slots" % number_of_slots)
        else:
            print("Please provide correct numbers of slots")
        return

    def get_available_slot(self):
        """sorted available parking
        """
        available_slots = filter(lambda x: x.is_available, self.slots.values())
        if not available_slots:
            return None
        print(self.slots.values())
        return sorted(available_slots, key=lambda x: x.slot_number)[0]

    def park(self, register_number, color):
        """park a new car in available parking slot.
        :param register_number - String
        :param color - String
        """

        if len(self.slots) == 0:
            print("Parking Lot not created")
            return

        available_slot = self.get_available_slot()

        # update new parking car
        if available_slot:
            # create new car object
            available_slot.car = car.Car.create(register_number, color)
            available_slot.is_available = False
            print("Allocated slot number: %s" % available_slot.slot_number)
        else:
            print("Sorry, parking lot is full.")

    def leave(self, slot_number):
        """update slot into available once parking_car leaves
        :param slot_number Integer
        """
        slot_number = int(slot_number)

        if slot_number in self.slots:
            parking_slot = self.slots[slot_number]
            if not parking_slot.is_available and parking_slot.car:
                parking_slot.car = None
                parking_slot.is_available = True
                print("Slot number %s is free" % slot_number)
            else:
                print("No car is present at slot number %s" % slot_number)
        else:
            print("Sorry, slot number does not exist in parking lot.")

    def status(self):
        """show parking status
        """

        print("Slot No\tRegistration No\tColor")
        for slot in self.slots.values():
            if not slot.is_available and slot.car:
                print("%s\t%s\t%s" % (slot.slot_number, slot.car.registration_number, slot.car.colour))

    def registration_numbers_for_cars_with_color(self, color):
        """get registration numbers of car from color
        :param color: car color - String
        """

        register_numbers = ''
        for parking_slots in self.slots.values():
            if not parking_slots.is_available and parking_slots.car and \
                    parking_slots.car.color == color:
                register_numbers += '%s ' % register_numbers.car.reg_no

        if register_numbers:
            print(register_numbers[:-1])
        else:
            print("Not found")

    def slot_numbers_for_cars_with_colour(self, colour):
        """find slot numbers with colour
        :param colour: string
        """

        slot_number = ''
        for pslot in self.slots.values():
            if not pslot.is_available and pslot.car and \
                    pslot.car.colour == colour:
                slot_number += '%s ' % pslot.slot_number

        if slot_number:
            print(slot_number[:-1])
        else:
            print("Not found")

    def slot_number_for_registration_number(self, register_number):
        """find slot number from registration number
        :param register_number - string
        """

        slot_number = ''
        for pslot in self.slots.values():
            if not pslot.available and pslot.car and \
                    pslot.car.reg_no == pslot:
                slot_number = pslot.slot_number
                break

        if slot_number:
            print(slot_number)
        else:
            print("Not found")
