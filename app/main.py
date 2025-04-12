from config import knights_config
from app.knight import Knight
from app.battle import fight
from typing import Dict


def battle() -> Dict[str, int]:
    # Створення об'єктів Knight
    knights = {name: Knight(config) for name, config in knights_config.items()}

    # Проведення боїв
    fights = [("lancelot", "mordred"), ("arthur", "red_knight")]
    for name1, name2 in fights:
        fight(knights[name1], knights[name2])

    # Повернення результатів
    return {knight.name: knight.hp for knight in knights.values()}