"""Base class for every fighter. Owner: Sean (Collado).

Concepts shown here:
- Abstraction:  Character is an abstract class; special_attack() must be written by each subclass.
- Encapsulation: stats and HP are private (_name) and read through properties.
"""
import random
from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, pow, dex, defense, hea, lck):
        self._name = name
        self._pow = pow          # Power: attack damage
        self._dex = dex          # Dexterity: chance (%) to dodge
        self._def = defense      # Defense: reduces damage taken
        self._hea = hea          # Health: max HP = HEA * 10
        self._lck = lck          # Luck: chance (%) to crit
        self._hp = self.max_hp

    # ----- encapsulation: read-only access -----
    @property
    def name(self):
        return self._name

    @property
    def pow(self):
        return self._pow

    @property
    def dex(self):
        return self._dex

    @property
    def defense(self):
        return self._def

    @property
    def hea(self):
        return self._hea

    @property
    def lck(self):
        return self._lck

    @property
    def max_hp(self):
        return self._hea * 10

    @property
    def hp(self):
        return self._hp

    def is_alive(self):
        return self._hp > 0

    def take_damage(self, amount):
        self._hp = max(0, self._hp - amount)

    def heal(self, amount):
        self._hp = min(self.max_hp, self._hp + amount)

    # ----- shared attack logic (subclasses reuse this) -----
    def _deal(self, target, multiplier=1.0, label="attacks",
              ignore_defense=False, force_crit=False, extra_dodge=0):
        """Hit the target once and return a message for the battle log."""
        if random.random() * 100 < target.dex + extra_dodge:
            return f"{self.name} {label}, but {target.name} dodged!"
        damage = self._pow * multiplier
        crit = force_crit or random.random() * 100 < self._lck
        if crit:
            damage *= 1.5
        if not ignore_defense:
            damage -= target.defense / 2
        damage = max(1, int(damage))
        target.take_damage(damage)
        text = f"{self.name} {label} {target.name} for {damage} damage"
        return text + (" (CRIT!)" if crit else "") + "."

    # ----- the three methods from the requirements -----
    def attack(self, target):
        """Normal attack."""
        return self._deal(target, 1.0, "attacks")

    def heavy_attack(self, target):
        """Heavy attack: hits harder but is easier to dodge."""
        return self._deal(target, 1.8, "smashes", extra_dodge=20)

    @abstractmethod
    def special_attack(self, target):
        """Each class has its own special attack (polymorphism)."""
