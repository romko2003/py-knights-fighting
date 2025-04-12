class Weapon:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power


class Armour:
    def __init__(self, part: str, protection: int):
        self.part = part
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: dict):
        self.name = name
        self.effect = effect