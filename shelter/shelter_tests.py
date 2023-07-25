import unittest
from enum import Enum
from datetime import date
from shelter import RegistrationRecord, DonationRegistry
from shelter import DonationType


class DonatorReportTestCase(unittest.TestCase):

    def test_given_donator_report_aggregates_multiple_records_by_name(self):
        records = [
            RegistrationRecord(
                "Alex Black", DonationType.MONEY, 100, date(2023, 7, 2)),
            RegistrationRecord(
                "Kate White", DonationType.CLOTHING, 14, date(2023, 6, 2)),
            RegistrationRecord(
                "Sue Green", DonationType.MONEY, 5, date(2023, 6, 2)),
            RegistrationRecord(
                "Ann Blue", DonationType.MONEY, 70, date(2023, 7, 2)),
            RegistrationRecord(
                "Ann Blue", DonationType.MONEY, 7, date(2023, 7, 2))
        ]
        registry = DonationRegistry()

        for record in records:
            registry.add_registry(record)

        res = registry.donator_report()
        self.assertEqual(
            res, {'Alex Black': 1, 'Kate White': 1, 'Sue Green': 1, 'Ann Blue': 2})

    def test_given_empty_registry_returns_empty_report(self):
        registry = DonationRegistry()
        res = registry.donator_report()
        self.assertEqual(
            res, {})


class InventoryReportTestCase(unittest.TestCase):

    def test_given_inventory_report_aggregates_multiple_records_by_type(self):
        records = [
            RegistrationRecord(
                "Alex Black", DonationType.MONEY, 100, date(2023, 7, 2)),
            RegistrationRecord(
                "Kate White", DonationType.CLOTHING, 14, date(2023, 6, 2)),
            RegistrationRecord(
                "Sue Green", DonationType.MONEY, 5, date(2023, 6, 2)),
            RegistrationRecord(
                "Ann Blue", DonationType.MONEY, 70, date(2023, 7, 2)),
            RegistrationRecord(
                "Ann Blue", DonationType.MONEY, 7, date(2023, 7, 2))
        ]
        registry = DonationRegistry()

        for record in records:
            registry.add_registry(record)

        res = registry.donations_inventory_report()
        self.assertEqual(
            res, {DonationType.MONEY: 182, DonationType.CLOTHING: 14})

    def test_given_empty_registry_returns_empty_report(self):
        registry = DonationRegistry()
        res = registry.donations_inventory_report()
        self.assertEqual(
            res, {})


class DonationDistributionTestCase(unittest.TestCase):

    def test_given_donation_distribution_aggregates_multiple_records_by_date_and_type(self):
        records = [
            RegistrationRecord(
                "Alex Black", DonationType.MONEY, 100, date(2023, 7, 2)),
            RegistrationRecord(
                "Kate White", DonationType.CLOTHING, 14, date(2023, 6, 2)),
            RegistrationRecord(
                "Sue Green", DonationType.MONEY, 5, date(2023, 6, 2)),
            RegistrationRecord(
                "Ann Blue", DonationType.MONEY, 70, date(2023, 7, 2)),
            RegistrationRecord(
                "Jack Yellow", DonationType.MONEY, 7, date(2023, 7, 2))
        ]
        registry = DonationRegistry()

        for record in records:
            registry.add_registry(record)

        res = registry.donation_distribution()
        self.assertEqual(
            res, {date(2023, 6, 2): {DonationType.MONEY: 5, DonationType.CLOTHING: 14}, date(2023, 7, 2): {DonationType.MONEY: 177}})

    def test_given_empty_registry_returns_empty_report(self):
        registry = DonationRegistry()
        res = registry.donation_distribution()
        self.assertEqual(
            res, {})


if __name__ == '__main__':
    unittest.main(verbosity=2)
