"""Tank class. Owner: Collado."""
from character import Character


class Tank(Character):
    def __init__(self, name="Tank"):
        super().__init__(name, pow=8, dex=4, defense=14, hea=18, lck=5)

    def special_attack(self, target):
        # TODO (Collado): make this your own. Starter: Shield Bash, hits and heals 5 HP.
        message = self._deal(target, 1.2, "uses Shield Bash on")
        self.heal(5)
        return message
