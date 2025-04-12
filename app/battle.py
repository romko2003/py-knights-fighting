from app.knight import Knight


def knights_battle(knights: list[Knight]) -> dict:
    results = {knight.name: 0 for knight in knights}

    for i, knight in enumerate(knights):
        for j, opponent in enumerate(knights):
            if i == j:
                continue
            damage = max(0, knight.power - opponent.protection)
            opponent.hp -= damage

    for knight in knights:
        if knight.hp > 0:
            results[knight.name] = knight.hp

    return results
