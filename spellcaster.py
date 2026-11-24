"""Spellcaster class. Owner: Estillore."""
from character import Character


class Spellcaster(Character):
    def __init__(self, name="Spellcaster"):
        super().__init__(name, pow=16, dex=6, defense=4, hea=10, lck=8)

    def special_attack(self, target):
        # TODO (Estillore): make this your own. Starter: Arcane Blast, ignores defense.
        return self._deal(target, 1.5, "casts Arcane Blast on", ignore_defense=True)
