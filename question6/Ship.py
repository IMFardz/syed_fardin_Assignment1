"""Implementation of Superclass Ship"""


class Ship:
    """An instance of type Ship to be used in the game"""

    shield_strength: float
    hull_strength: float
    laser_power: float
    name: str
    alive: bool

    def __init__(self, name) -> None:
        """Create a new instance of Ship"""
        self.alive = True
        self.name = name
        self.laser_power = 5
        self.hull_strength = 10
        self.shield_strength = 10

    def __str__(self):
        return "Name:{}  Hull Strength: {}  Shield Power {}".format(self.name, self.hull_strength, self.shield_strength)

    def take_hit(self, attack_power) -> None:
        """Modifies ship status after taking a hit"""
        if self.shield_strength != 0:
            if self.shield_strength < attack_power:
                self.hull_strength -= 0.5 * (attack_power -self.shield_strength)
                self.shield_strength = 0
                if self.hull_strength <= 0:
                    self.alive = False
            else:
                self.shield_strength -= attack_power
        else:
            self.hull_strength -= 0.5 * attack_power
            if self.hull_strength <= 0:
                self.alive = False

    def attack(self, other_ship: "Ship"):
        """Attacks other ship"""
        other_ship.take_hit(self.laser_power)
