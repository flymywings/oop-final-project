import unittest

from battle import Battle
from hero import Hero


class MarvelHero(Hero):
    def use_skill(self, opponent):
        return self.skill_attack(opponent, "Marvel Blast")


class DCHero(Hero):
    def use_skill(self, opponent):
        return self.skill_attack(opponent, "DC Strike")


class BattleTests(unittest.TestCase):
    def setUp(self):
        self.battle = Battle()
        self.marvel = MarvelHero("Marvel Hero", 25)
        self.dc = DCHero("DC Hero", 20)

    def test_hero_is_abstract_and_health_stays_in_bounds(self):
        with self.assertRaises(TypeError):
            Hero("Base Hero", 25)

        self.assertEqual(self.marvel.heal(), "Marvel Hero heals 0 HP.")
        self.assertEqual(self.marvel.take_damage(120), 100)
        self.assertEqual(self.marvel.get_health(), 0)

    def test_turns_damage_healing_and_hero_specific_skills(self):
        self.battle.start(self.marvel, self.dc)

        self.battle.play("attack")
        self.assertEqual(self.dc.get_health(), 75)
        self.assertEqual(self.battle.current_turn, 2)

        self.battle.play("heal")
        self.assertEqual(self.dc.get_health(), 95)
        self.assertEqual(self.battle.current_turn, 1)

        self.battle.play("skill")
        self.assertEqual(self.dc.get_health(), 45)
        self.assertIn("Marvel Blast", self.battle.log[-1])

        self.battle.play("skill")
        self.assertEqual(self.marvel.get_health(), 60)
        self.assertIn("DC Strike", self.battle.log[-1])

    def test_winner_locks_actions_and_restart_clears_the_match(self):
        self.assertFalse(self.battle.play("attack"))
        self.battle.start(self.marvel, self.dc)
        self.assertFalse(self.battle.play("invalid"))
        self.assertEqual(self.battle.current_turn, 1)

        self.battle.play("skill")
        self.battle.play("attack")
        self.battle.play("skill")

        self.assertIs(self.battle.winner, self.marvel)
        self.assertEqual(self.dc.get_health(), 0)
        self.assertIsNone(self.battle.current_turn)
        self.assertFalse(self.battle.play("heal"))
        self.assertEqual(self.battle.log[-1], "Marvel Hero wins!")

        self.battle.restart()
        self.assertIsNone(self.battle.winner)
        self.assertIsNone(self.battle.marvel_hero)
        self.assertIsNone(self.battle.dc_hero)
        self.assertEqual(self.battle.log, [])
        self.assertFalse(self.battle.play("attack"))

        rematch_hero = DCHero("Another DC Hero", 20)
        self.battle.start(MarvelHero("Marvel Hero", 25), rematch_hero)
        self.assertEqual(rematch_hero.get_health(), 100)
        self.assertEqual(self.battle.current_turn, 1)


if __name__ == "__main__":
    unittest.main()
