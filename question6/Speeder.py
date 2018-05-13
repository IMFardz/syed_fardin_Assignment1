from Ship import Ship
from random import random


class Speeder(Ship):
    """An object of type Warship"""
    name: str
    alive: bool

    def __init__(self, name) -> None:
        """Creates a new instance of Warship"""
        super().__init__(name)

    def take_hit(self, attack_power) -> None:
        """Modifies speeder after taking a hit"""

        a = random()
        if a <= 0.5:
            pass
        else:
            super.attack(attack_power)
