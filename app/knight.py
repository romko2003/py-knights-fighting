class Knight:
    def __init__(self, config):
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]

    def take_damage(self, amount):
        self.hp -= amount