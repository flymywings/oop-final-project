from abc import ABC, abstractmethod


class Hero(ABC):
    MAX_HEALTH = 100

    def __init__(self, name, power):
        self.__name = name
        self.__power = power
        self.__health = self.MAX_HEALTH

    def get_name(self):
        return self.__name

    def get_power(self):
        return self.__power

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        previous_health = self.__health
        self.__health = max(0, self.__health - max(0, damage))
        return previous_health - self.__health

    def attack(self, opponent):
        damage = opponent.take_damage(self.__power)
        return f"{self.__name} attacks {opponent.get_name()} for {damage} damage."

    def heal(self):
        previous_health = self.__health
        self.__health = min(self.MAX_HEALTH, self.__health + 20)
        healed = self.__health - previous_health
        return f"{self.__name} heals {healed} HP."

    @abstractmethod
    def use_skill(self, opponent):
        """Perform this hero's special move and return a battle log message."""

    def skill_attack(self, opponent, skill_name):
        damage = opponent.take_damage(self.__power * 2)
        return f"{self.__name} uses {skill_name} for {damage} damage."
