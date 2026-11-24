"""Console version so the game can be played before the GUI exists. Owner: Sean (Collado).
The GUI (Solis) should replace this, using the same Battle object.
"""
from battle import Battle
from tank import Tank
from spellcaster import Spellcaster
from assassin import Assassin
from marksman import Marksman
from warrior import Warrior

CLASSES = {"Tank": Tank, "Spellcaster": Spellcaster, "Assassin": Assassin,
           "Marksman": Marksman, "Warrior": Warrior}
MENU = {"1": "attack", "2": "heavy_attack", "3": "special_attack"}


def pick(player_number):
    names = list(CLASSES)
    for i, name in enumerate(names, 1):
        print(f"  {i}. {name}")
    choice = int(input(f"Player {player_number}, pick a class: "))
    return CLASSES[names[choice - 1]](f"P{player_number} {names[choice - 1]}")


def main():
    battle = Battle()
    battle.start(pick(1), pick(2))
    while battle.current_turn is not None:
        p1, p2 = battle.player1, battle.player2
        print(f"\n{p1.name} HP {p1.hp}/{p1.max_hp} | {p2.name} HP {p2.hp}/{p2.max_hp}")
        print(f"Player {battle.current_turn}: 1 Attack, 2 Heavy attack, 3 Special")
        action = MENU.get(input("> ").strip())
        if action:
            print(battle.play(action))
    print(battle.log[-1])


if __name__ == "__main__":
    main()
