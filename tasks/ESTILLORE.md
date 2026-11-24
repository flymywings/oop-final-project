# Estillore: Assassin + battle screen

**Files:** `assassin.py`, `gui_battle.py`

## Checklist
- [ ] `assassin.py`: tune the stats and make your own `special_attack` (the starter is a guaranteed crit)
- [ ] `gui_battle.py`: the battle screen (details below)

## assassin.py
Keep the class extending `Character`. `special_attack(self, target)` must return a message string. Use `self._deal(...)` to hit; read its options in `character.py`. Assassin is the high-DEX, high-LCK fighter.

## gui_battle.py
Write a Tkinter frame with this exact signature so it plugs into `gui.py`:

```python
class BattleScreen(tk.Frame):
    def __init__(self, parent, battle, on_restart):
        # battle: the Battle object, already started
        # on_restart: function you call when Restart is clicked (no arguments)
    def refresh(self):
        # redraw everything from the battle's current state
```

Show, reading from `battle`:
- Both fighters' names and HP: `battle.player1.name`, `battle.player1.hp`, `battle.player1.max_hp` (same for `player2`). A label like "42/100" is enough; a progress bar is a bonus.
- Whose turn it is: `battle.current_turn` (1 or 2).
- The battle log: `battle.log` (a list of strings).
- The winner: `battle.winner` (a character, or `None`). Show `battle.winner.name`.

Buttons:
- **Attack**, **Heavy Attack**, **Special Attack** call `battle.play("attack")`, `battle.play("heavy_attack")`, `battle.play("special_attack")`, then `self.refresh()`.
- Disable the three buttons when `battle.current_turn is None` (match is over).
- **Restart** calls `on_restart()`.

Test it alone with a small script: build two fighters, `Battle().start(...)`, and show your frame.

## Git
```text
git clone https://github.com/flymywings/oop-final-project
cd oop-final-project
git checkout -b estillore
# edit only your files, then:
python -m unittest -v
git add assassin.py gui_battle.py
git commit -m "Assassin and battle screen"
git push -u origin estillore
```

## Done when
Pushed by **Tuesday night**, finished by **Wednesday noon**.
