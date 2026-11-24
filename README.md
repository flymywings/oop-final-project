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
| **Collado** | `character.py`, `battle.py`, `main.py` | Base class, battle rules, merging everyone's branches, final run-through |
| **Dagaerag** | `tank.py`, `warrior.py` | Finish both classes: tune stats, write a unique `special_attack` |
| **Estillore** | `spellcaster.py`, `marksman.py` | Finish both classes: tune stats, write a unique `special_attack` |
| **Fajardo** | `assassin.py`, `test_battle.py` | Finish Assassin, add tests for every class, write the final report/slides for the rubric |
| **Solis** | `gui.py` | Tkinter or pygame screen: pick a class per player, HP bars, 3 action buttons, battle log, winner, restart |

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
