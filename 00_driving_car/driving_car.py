""" 
Create a car that can drive when it has a petrol in a tank (variable).
The user can add petrol by calling the appropriate method.
The petrol consumption depends on a distance and is calculated accordingly: 1(L) per 10(km).

NOTE:   Let's say tank capacity is 90.
        New car has no petrol in its tank.

 """


class Car():

    def __init__(self):
        self._current_volume_l = 0
        self.petrol_consumption = 10

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
