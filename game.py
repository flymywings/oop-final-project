import sys

from battle import Battle
from hero import Hero


def main():
    import tkinter as tk

    try:
        from arena_ui import ArenaUI
        from dc import DC_ROSTER
        from marvel import MARVEL_ROSTER
    except ModuleNotFoundError as error:
        if error.name not in ("arena_ui", "dc", "marvel"):
            raise
        sys.exit(f"Waiting for {error.name}.py. Try: python game.py --demo")

    root = tk.Tk()
    root.title("Marvel vs DC Battle Arena")
    ArenaUI(root, Battle(), MARVEL_ROSTER, DC_ROSTER)
    root.mainloop()


class DemoHero(Hero):
    def __init__(self, name, power, skill_name):
        super().__init__(name, power)
        self.skill_name = skill_name

    def use_skill(self, opponent):
        return self.skill_attack(opponent, self.skill_name)


def run_demo():
    battle = Battle()
    iron_man = DemoHero("Iron Man", 25, "Repulsor Blast")
    batman = DemoHero("Batman", 20, "Batarang Throw")
    battle.start(iron_man, batman)
    print(battle.log[-1])

    for action in ("attack", "heal", "skill", "attack", "skill"):
        previous_log_length = len(battle.log)
        battle.play(action)
        for message in battle.log[previous_log_length:]:
            print(message)
        print(f"Iron Man HP: {iron_man.get_health()} | Batman HP: {batman.get_health()}")

    battle.restart()
    print("Match reset. Ready for hero selection.")


if __name__ == "__main__":
    if sys.argv[1:] == ["--demo"]:
        run_demo()
    else:
        main()
