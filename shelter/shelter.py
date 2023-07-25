from enum import Enum
from datetime import date
from typing import Dict


class DonationType(Enum):
    MONEY = 1
    FOOD = 2
    CLOTHING = 3
    OTHER = 4


class RegistrationRecord():
    '''
    Data structure that contains attributes for donation record.
    '''

    def __init__(self, donor_name: str, donation_type: DonationType, quantity: int, date: date):
        self.donor_name = donor_name
        self.donation_type = donation_type
        self.quantity = quantity
        self.date = date


class DonationRegistry():
    '''
    Class that stores donation records and provides reporting functionality.
    '''

    def __init__(self):
        self.donation_registry = []

    def add_registry(self, record: RegistrationRecord):
        self.donation_registry.append(record)

    def donation_distribution(self) -> Dict[date, Dict[DonationType, int]]:
        '''
        Donation Distribution captures the type of donation, quantity, and the date of distribution.
        Result is aggregated by date and within it by type.
        '''
        result = {}
        for record in self.donation_registry:
            if record.date in result:
                if record.donation_type in result[record.date]:
                    result[record.date][record.donation_type] += record.quantity
                else:
                    result[record.date][record.donation_type] = record.quantity
            else:
                result[record.date] = {record.donation_type: record.quantity}
        return result

    def get_registry(self):
        return self.donation_registry

    def donations_inventory_report(self) -> Dict[DonationType, int]:
        '''
        An inventory report displays the current status of donations, grouped by type.
        Report shows type and its quantity.
        '''
        report = {}
        for record in self.donation_registry:
            if record.donation_type in report:
                report[record.donation_type] += record.quantity
            else:
                report[record.donation_type] = record.quantity
        return report

    def donator_report(self) -> Dict[str, int]:
        '''
        A donator report summarizes the total contributions received from each donor.
        '''
        report = {}
        for record in self.donation_registry:
            if record.donor_name in report:
                report[record.donor_name] += 1
            else:
                report[record.donor_name] = 1
        return report


def main():
    '''
    sample code that shows how to use the library
    '''
    # create records
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

    # create registry for records
    registry = DonationRegistry()

    for record in records:
        # add records into registry
        registry.add_registry(record)

    # shows donation distribution by date, then by type
    print(registry.donation_distribution())
    # shows inventory report by type and quantity
    print(registry.donations_inventory_report())
    # shows total donator report distribution
    print(registry.donator_report())


if __name__ == '__main__':
    main()
