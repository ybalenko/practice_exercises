import unittest
from driving_car import Car


class DrivingCarTestCase(unittest.TestCase):

    def test_given_new_car_can_not_drive(self):
        car = Car()
        res = car.drive(1)
        self.assertFalse(res)

    def test_given_new_car_fill_tank_car_can_drive(self):
        car = Car()
        car.add_petrol(1)
        res = car.drive(1)
        self.assertTrue(res, "Car cannot drive")

    def test_given_not_enought_petrol_car_can_not_drive(self):
        car = Car()
        car.add_petrol(1)
        res1 = car.drive(10)
        self.assertTrue(res1)
        res2 = car.drive(10)
        self.assertFalse(res2, "Unexpected result: car should not drive")

    def test_given_driver_can_not_add_too_much_petrol(self):
        car = Car()
        res = car.add_petrol(100)
        self.assertFalse(res, "Unexpected result: can not add too much petrol")

    def test_given_driver_can_not_add_petrol_several_times_over_capacity(self):
        car = Car()
        res1 = car.add_petrol(50)
        self.assertTrue(res1)
        res2 = car.add_petrol(50)
        self.assertFalse(
            res2, "Unexpected result: can not add too much petrol")
        res3 = car.get_current_volume()
        self.assertEquals(50, res3, "Unexpected petrol volume")


if __name__ == '__main__':
    unittest.main(verbosity=2)
