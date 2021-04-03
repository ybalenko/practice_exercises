"""  
Create a worker who can go to the office. A worker must have a name and an age.
A worker has to be able to make a decision whether to go to the office or not depending on a day/schedule.

NOTE: Let's say a worker works on weekdays only.
"""
from datetime import date
from calendar import Calendar


class Worker():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def go_to_office(self, day: date) -> bool:
        self.day = day
        weekday_number = day.weekday()
        if weekday_number in range(0, 5):
            return True
        else:
            return False
