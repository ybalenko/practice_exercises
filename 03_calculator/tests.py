import unittest
from main import Calculator, UndefinedResultError


class CalcTestCase(unittest.TestCase):

    def test_add_given_numbers_returns_sum(self):
        calc = Calculator()
        res = calc.add(2, 5)
        self.assertEqual(7, res)

    def test_add_with_negative_number_returns_sum(self):
        calc = Calculator()
        res = calc.add(-9, 3549)
        self.assertEqual(3540, res)

    def test_substract_smaller_number_from_larger_obtains_difference(self):
        calc = Calculator()
        res = calc.sub(900, 5)
        self.assertEqual(895, res)

    def test_substract_larger_number_from_smaller_obtains_difference(self):
        calc = Calculator()
        res = calc.sub(5, 55)
        self.assertEqual(-50, res)

    def test_divide_without_remainder(self):
        calc = Calculator()
        res = calc.div(55, 5)
        self.assertEqual(11, res)

    def test_divide_with_remainder(self):
        calc = Calculator()
        res = calc.div(3, 2)
        self.assertEqual(1.5, res)

    def test_divide_by_zero_returns_error(self):
        calc = Calculator()
        try:
            calc.div(12, 0)
            self.assertFalse(True, "Expected exception")
        except:
            return

    def test_divide_by_negative_number_returns_negative(self):
        calc = Calculator()
        res = calc.div(15, -3)
        self.assertEqual(-5, res)

    def test_divide_zero_by_non_zero(self):
        calc = Calculator()
        res = calc.div(0, 3)
        self.assertEqual(0, res)

    def test_multiply_two_positive_numbers_returns_positive(self):
        calc = Calculator()
        res = calc.multi(8, 3)
        self.assertEqual(24, res)

    def test_multiply_positive_and_negative_returns_negative(self):
        calc = Calculator()
        res = calc.multi(15, -3)
        self.assertEqual(-45, res)

    def test_multiply_any_number_and_zero_returns_zero(self):
        calc = Calculator()
        res = calc.multi(15, 0)
        self.assertEqual(0, res)

    # Any number raised to the power of 0, except 0, equals 1.

    def test_number_raised_to_power_of_0_equals_1(self):
        calc = Calculator()
        res = calc.power(2, 0)
        self.assertEqual(1, res)

    # Any number raised to the power of 1 equals the number itself.
    def test_number_raised_to_power_of_1_equals_this_number(self):
        calc = Calculator()
        res = calc.power(234, 1)
        self.assertEqual(234, res)

    # A number to the power of negative one is equal to one over that number.
    def test_number_raised_to_power_of_negative_returns_fraction(self):
        calc = Calculator()
        res = calc.power(2, -1)
        self.assertEqual(0.5, res)

    # 0 to the power of 0 returns error
    def test_zero_to_power_of_zero_returns_error(self):
        calc = Calculator()
        try:
            calc.power(0, 0)
            self.assertFalse(True, "Expected exception")
        except UndefinedResultError:
            return
        except:
            self.assertFalse(True, "Unexpected type of exception")

    # 0 to the power of negative one returns error
    def test_zero_to_power_of_negative_returns_error(self):
        calc = Calculator()
        try:
            calc.power(0, -1)
            self.assertFalse(True, "Expected exception")
        except UndefinedResultError:
            return
        except:
            self.assertFalse(True, "Unexpected type of exception")


if __name__ == '__main__':
    unittest.main(verbosity=2)
