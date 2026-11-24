"""Marksman class. Owner: Estillore."""
from character import Character


class Marksman(Character):
    def __init__(self, name="Marksman"):
        super().__init__(name, pow=15, dex=12, defense=5, hea=10, lck=10)

    def special_attack(self, target):
        # TODO (Estillore): make this your own. Starter: Double Shot, two hits at 0.7x.
        first = self._deal(target, 0.7, "fires a Double Shot at")
        second = self._deal(target, 0.7, "fires a Double Shot at")
        return first + " " + second
