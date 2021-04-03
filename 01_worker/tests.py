import unittest
from datetime import date
from office_worker import Worker


class GoOrNotToOfficeTestCase(unittest.TestCase):

    def test_on_weekend_worker_does_not_go_to_office(self):
        alex = Worker("Alex", 25)
        day = date(2021, 4, 3)
        res = alex.go_to_office(day)
        self.assertFalse(res)

    def test_on_weekday_worker_goes_to_office(self):
        alex = Worker("Alex", 25)
        day = date(2021, 4, 5)
        res = alex.go_to_office(day)
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main(verbosity=2)
