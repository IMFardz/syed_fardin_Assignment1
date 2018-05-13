from Ship import Ship
from random import random

class Warship(Ship):
    """An object of type Warship"""
    name: str
    alive: bool

    shield_strength = 10
    hull_strength = 10
    laser_power = 5
    high_power_bonus = 5

    def __init__(self, name) -> None:
        """Creates a new instance of Warship"""
        super().__init__(name, Warship.laser_power, Warship.hull_strength, Warship.shield_strength)

    def attack(self, other_ship) -> None:
        """Attack other_ship"""
        a = random()
        if a <= 0.3:
            self.laser_power += Warship.high_power_bonus

        super.attack(other_ship)

        self.laser_power -= Warship.high_power_bonus
