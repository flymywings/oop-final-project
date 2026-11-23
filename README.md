# Marvel vs DC Battle Arena

A two-player Python game. Player 1 picks a Marvel hero, Player 2 picks a DC hero, and they take turns using Attack, Use Skill, or Heal.

## Run the leader's starter

```text
python game.py --demo
python -m unittest -v
```

The console demo uses temporary versions of Iron Man and Batman to show attack, healing, skills, a winner, and restart. Run `python game.py` to launch Tkinter once the roster and GUI files are ready. If your computer uses `py` for Python, use it in place of `python`. On the leader's computer, run `uv run --no-project python game.py --demo`.

## Team handoff

1. **Sean** owns `hero.py`, `battle.py`, and `game.py`. Sean handles the battle rules and puts everyone's code together. Heroes start at 100 HP, Attack deals the hero's power, the default skill deals double power, and Heal restores up to 20 HP.
2. **Both rosters** owns `marvel.py` and `dc.py`. Make Iron Man and Batman first. Then add Thor, Spider-Man, and Captain America to `MARVEL_ROSTER`, and Superman, Flash, and Wonder Woman to `DC_ROSTER`.
3. **Hero selection screen** owns `hero_select_ui.py`. Build the Marvel and DC hero buttons, show which heroes are selected, and add a Start button.
4. **Battle screen** owns `arena_ui.py`. Show HP, the current turn, the battle log, and the winner. Add Attack, Use Skill, Heal, and Restart buttons. Switch between the selection and battle screens.
5. **Equipment and teams** owns `equipment.py` and `team.py`. Make the Weapon, Skill, Item, Inventory, and Team classes. Coordinate with Sean so heroes use weapons (association), own their inventories (composition), and can join teams (aggregation). Let multiple heroes use the same shared skill object.

### For the roster owner

Subclass `Hero`. Give each subclass a constructor that takes no arguments and an override of `use_skill(opponent)` that returns a message for the battle log. Each roster is a dictionary that maps display names to classes.

```python
from hero import Hero


class IronMan(Hero):
    def __init__(self):
        super().__init__("Iron Man", 25)

    def use_skill(self, opponent):
        return self.skill_attack(opponent, "Repulsor Blast")


MARVEL_ROSTER = {"Iron Man": IronMan}
```

### For the hero selection screen owner

Build `HeroSelectUI(parent, marvel_roster, dc_roster, on_start)` as a Tkinter frame. List Marvel on the left and DC on the right. Highlight one pick per side and enable Start once both sides have a selection. When Start is clicked, call `on_start(marvel_pick, dc_pick)` with the two selected names.

### For the battle screen owner

Build `ArenaUI(root, battle, marvel_roster, dc_roster)`. Create the selection frame and pass it your Start callback. `game.py` creates the Tkinter window and runs the event loop.

- **Start.** Call `battle.start(marvel_roster[marvel_pick](), dc_roster[dc_pick]())` and show the battle screen. The parentheses create fresh heroes with full HP.
- **Act.** Send `battle.play("attack")`, `battle.play("skill")`, or `battle.play("heal")` and refresh the display. Each valid action uses one turn.
- **Refresh.** Read `battle.marvel_hero` and `battle.dc_hero` for the heroes. Use `get_name()` and `get_health()` on each. Show `battle.log` as the action history, `battle.current_turn` as Player 1 or 2, and `battle.winner.get_name()` when there is a winner. The turn is `None` before a match and after a win. Disable actions in both cases.
- **Restart.** Call `battle.restart()` and show a fresh selection frame. Clear the HP display, log, and winner from the old match.

Work on one Git branch per person. First merge enough to play Iron Man vs Batman with the mouse, then add the remaining heroes and connect the equipment and teams.
