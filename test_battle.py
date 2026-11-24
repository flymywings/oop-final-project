import random
import unittest

from battle import Battle
from character import Character
from tank import Tank
from spellcaster import Spellcaster
from assassin import Assassin
from marksman import Marksman
from warrior import Warrior


class TestCharacters(unittest.TestCase):
    def setUp(self):
        random.seed(1)

    def test_character_is_abstract(self):
        with self.assertRaises(TypeError):
            Character("x", 1, 1, 1, 1, 1)

    def test_encapsulation_hp_is_read_only(self):
        tank = Tank()
        with self.assertRaises(AttributeError):
            tank.hp = 0

    def test_every_class_has_three_actions(self):
        for cls in (Tank, Spellcaster, Assassin, Marksman, Warrior):
            fighter, enemy = cls(), Warrior()
            for action in Battle.ACTIONS:
                self.assertIsInstance(getattr(fighter, action)(enemy), str)


class TestBattle(unittest.TestCase):
    def test_battle_reaches_a_winner(self):
        random.seed(2)
        battle = Battle()
        battle.start(Spellcaster(), Tank())
        for _ in range(500):
            if battle.current_turn is None:
                break
            battle.play("special_attack")
        self.assertIsNotNone(battle.winner)
        self.assertIsNone(battle.current_turn)

    def test_restart_clears_everything(self):
        battle = Battle()
        battle.start(Tank(), Warrior())
        battle.play("attack")
        battle.restart()
        self.assertEqual(battle.log, [])
        self.assertIsNone(battle.winner)


if __name__ == "__main__":
    unittest.main()
