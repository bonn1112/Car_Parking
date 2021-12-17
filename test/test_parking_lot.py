import unittest
import sys
import os
import read_file

from Car_Parking.src import parking


class TestParkingLot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parking = parking.Parking()
        cls.allocated_slot = 1

    def test_create_parking_lot(self):
        self.parking.create_parking_lot(6)
        self.assertEqual(len(self.parking.slots), 6, msg="Wrong numbers of parking")

    def test_park(self):
        self.parking.park("MH-12-FF-2017", "Black")
        self.assertFalse(self.parking.slots[self.allocated_slot].is_available, "Park failed.")
        for i in self.parking.slots.values():
            if not i.is_available and i.car:
                self.assertEqual(i.car.registration_number, "MH-12-FF-2017", "Park failed")
                self.assertEqual(i.car.colour, "Black", "Park failed")

    def test_leave(self):
        self.parking.leave(self.allocated_slot)
        self.assertTrue(self.parking.slots[self.allocated_slot].is_available, "Leave failed.")

    @classmethod
    def tearDownClass(cls):
        del cls.parking


if __name__ == '__main__':
    unittest.main()
