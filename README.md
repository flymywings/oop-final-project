# OOP Final Project: Class Battle Arena

Due: **Thursday, Nov 26, 2026**. Group: Collado, Dagaerag, Estillore, Fajardo, Solis.

A two-player turn-based battle. Each player picks one of five classes, then takes turns using
**Attack**, **Heavy Attack**, or **Special Attack** until one fighter reaches 0 HP.

## Attributes (every character has all five)

| Attr | Meaning in the game |
|---|---|
| POW | Attack damage |
| DEX | % chance to dodge an attack |
| DEF | Reduces damage taken (DEF / 2 per hit) |
| HEA | Max HP = HEA x 10 |
| LCK | % chance to land a crit (1.5x damage) |

## Classes

Tank, Spellcaster, Assassin, Marksman, Warrior. Each one is a subclass of `Character`.

## Where the rubric is shown

| Concept | Where |
|---|---|
| Encapsulation | `character.py`: private `_pow`, `_hp`, etc., read through `@property` |
| Abstraction | `character.py`: `Character(ABC)` with abstract `special_attack()` |
| Inheritance | the five class files all extend `Character` |
| Polymorphism | each class overrides `special_attack()`; `battle.py` calls the same method on any class |

## Who does what

| Member | Files | Job |
|---|---|---|
| **Collado** | `character.py`, `battle.py`, `main.py`, `gui.py`, `tank.py` | Base class and battle rules (done), main window, Tank, merging, final run-through |
| **Dagaerag** | `spellcaster.py`, `gui_select.py` | Spellcaster + the class selection screen |
| **Estillore** | `assassin.py`, `gui_battle.py` | Assassin + the battle screen (HP, turn, 3 buttons, log, winner, restart) |
| **Fajardo** | `marksman.py`, `test_battle.py` | Marksman + tests for every class |
| **Solis** | `warrior.py`, `REPORT.md` | Warrior + the rubric report and slides |

**Everyone: open your own file in `tasks/` (for example `tasks/DAGAERAG.md`). It has your checklist, exact code contract, and git steps.**

The GUI is Tkinter only (no pygame).

## Rules for working together

1. One branch per person: `git checkout -b yourname`. Only edit your own files.
2. Do not change `character.py` or `battle.py`. If you need a change, message Collado.
3. Every class needs a no-argument-friendly constructor (`Tank()`) and a `special_attack(self, target)` that returns a log message string.
4. The GUI only talks to `Battle`: `start(p1, p2)`, `play("attack" | "heavy_attack" | "special_attack")`, `restart()`, and reads `p1.hp`, `p1.max_hp`, `current_turn`, `log`, `winner`.
5. Run `python -m unittest -v` before you push.

## Timeline

| When | Goal |
|---|---|
| Tue night | Everyone clones, makes a branch, pushes their first version |
| Wed noon | All classes and the GUI are merged into one working game |
| Wed night | Tests pass, bugs fixed, report/slides drafted |
| Thursday | Present |

## Run

```text
python main.py        # console version
python -m unittest -v # tests
```
