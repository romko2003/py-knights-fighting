def fight(knight1, knight2):
    knight1.take_damage(knight2.power)
    knight2.take_damage(knight1.power)