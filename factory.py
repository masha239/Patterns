class Airplane:
    def __init__(self, speed: int, size: int):
        self._speed = speed
        self._size = size

    def fly(self):
        print("Just flying there...")

class CivilianAirplane(Airplane):
    def __init__(self, speed: int, size: int, equipment: str):
        super().__init__(speed, size)
        self._equipment = equipment

    def fly(self):
        print("I care about people. I have " + self._equipment)


class MilitaryAirplane(Airplane):
    def __init__(self, speed: int, size: int, equipment: str):
        super().__init__(speed, size)
        self._equipment = equipment

    def fly(self):
        print("I can kill! I have " + self._equipment)


class PersonalAirplane(Airplane):
    def __init__(self, speed: int, size: int, equipment: str):
        super().__init__(speed, size)
        self._equipment = equipment

    def fly(self):
        print("Please, tell my owner that it's the last time I'm flying without " + self._equipment)


class Creator:
    def create(self, speed: int, size: int) -> Airplane:
        return Airplane(self, speed, size)


class CivilianCreator(Creator):
    def create(self, speed: int, size: int, equipment: str) -> Airplane:
        return CivilianAirplane(speed, size, equipment)


class MilitaryCreator(Creator):
    def create(self, speed: int, size: int, equipment: str) -> Airplane:
        return MilitaryAirplane(speed, size, equipment)

class PersonalCreator(Creator):
    def create(self, speed: int, size: int, equipment: str) -> Airplane:
        return PersonalAirplane(speed, size, equipment)


print("Let's make it right!")
creator = CivilianCreator()
equipment = "Coffee and tea"
plane = creator.create(700, 300, equipment)
plane.fly()

print("\nOK, now let's change our creator!")
creator = MilitaryCreator()
plane = creator.create(700, 300, equipment)
plane.fly()

print("\nInteresting! Well, how about this:")
creator = PersonalCreator()
equipment = "Guns and rockets"
plane = creator.create(700, 300, equipment)
plane.fly()

print("\nOK, it seems like everything works.")
