def fight(knight1, knight2):
    print(f"{knight1.name} vs {knight2.name} begins!")
    while knight1.hp > 0 and knight2.hp > 0:
        knight2.take_damage(knight1.power)
        if knight2.hp <= 0:
            print(f"{knight1.name} wins!")
            break
        knight1.take_damage(knight2.power)
        if knight1.hp <= 0:
            print(f"{knight2.name} wins!")
            break