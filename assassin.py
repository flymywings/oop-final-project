"""Assassin class. Owner: Fajardo."""
from character import Character


class Assassin(Character):
    def __init__(self, name="Assassin"):
        super().__init__(name, pow=14, dex=16, defense=5, hea=9, lck=12)

    def special_attack(self, target):
        # TODO (Fajardo): make this your own. Starter: Backstab, guaranteed crit.
        return self._deal(target, 1.0, "backstabs", force_crit=True)
