from app.equipment import Weapon, Armour, Potion


class Knight:
    def __init__(self, config: dict):
        self.name = config["name"]
        self.base_power = config["power"]
        self.hp = config["hp"]
        self.armour = [Armour(**a) for a in config.get("armour", [])]
        self.weapon = Weapon(**config["weapon"])
        self.potion = Potion(**config["potion"]) if config.get("potion") else None

        self._apply_equipment()

    def _apply_equipment(self):
        self.power = self.base_power + self.weapon.power
        self.protection = sum(a.protection for a in self.armour)

        if self.potion:
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)

    def take_damage(self, attacker_power):
        damage = max(0, attacker_power - self.protection)
        self.hp = max(0, self.hp - damage)