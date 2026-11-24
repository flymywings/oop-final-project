"""Warrior class. Owner: Dagaerag."""
from character import Character


class Warrior(Character):
    def __init__(self, name="Warrior"):
        super().__init__(name, pow=12, dex=8, defense=10, hea=14, lck=7)

    def special_attack(self, target):
        # TODO (Dagaerag): make this your own. Starter: Berserk Strike, 2x damage, 10 HP recoil.
        message = self._deal(target, 2.0, "uses Berserk Strike on")
        self.take_damage(10)
        return message
