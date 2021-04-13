""" 
Create a car that can drive when it has a petrol in a tank (variable).
The user can add petrol by calling the appropriate method.
The petrol consumption depends on a distance and is calculated accordingly: 1(L) per 10(km).

NOTE:   Let's say tank capacity is 90.
        New car has no petrol in its tank.

Additional task. English below.
Oписать метод переключения скорости.
Создать класс автомобиль с коробкой автомат. Сделать так, чтоб при вызове
метода переключения скоростей вызывалось исключение (если коробка автомат, то нельзя переключать передачи).

Describe the method of shifting the gears.
Create a class with automatic transmission. You can only shift gears if transmission is manual. If the gearbox is automatic, then you can not shift gears.
 """
from enum import Enum


class TransmissionType(Enum):
    AUTO = 0
    MANUAL = 1


class Car():

    def __init__(self, transmission: TransmissionType):
        self._current_volume_l = 0
        self.petrol_consumption = 10
        self.transmission = transmission

    def drive(self, distance_km: int) -> bool:
        self.distance_km = distance_km
        petrol_used = distance_km / self.petrol_consumption
        if self._current_volume_l >= petrol_used:
            self._current_volume_l = self._current_volume_l - petrol_used
            return True

        return False

    def add_petrol(self, new_volume_l: int) -> bool:
        if new_volume_l <= 90 - self._current_volume_l:
            self._current_volume_l = self._current_volume_l + new_volume_l
            return True
        else:
            return False

    def get_current_volume(self) -> int:
        return self._current_volume_l

    def shift_gear(self):
        if self.transmission == TransmissionType.MANUAL:
            return True
        else:
            raise Exception("Cannot shift gears for automatic transmission")
