class Person:
    def __init__(self, city_population, room_number):
        self._city_population = city_population
        self._room_number = room_number

    @property
    def person_room(self):
        return self._room_number

    @property
    def city_population(self):
        return self._city_population
