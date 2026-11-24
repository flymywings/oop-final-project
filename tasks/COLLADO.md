# Collado: base code, window, merging, Tank

**Files:** `character.py`, `battle.py`, `main.py` (done), `gui.py`, `tank.py`

## Checklist
- [x] `character.py`: abstract `Character` with the five attributes (encapsulation, abstraction)
- [x] `battle.py`: turn loop that works with any class (polymorphism)
- [x] `main.py`: console version
- [ ] `tank.py`: tune the stats and make your own `special_attack`
- [ ] `gui.py`: the main Tkinter window that connects Dagaerag's and Estillore's screens (details below)
- [ ] Merge everyone's branches into `master` by **Wednesday noon**
- [ ] Final run-through: play every class against every other class once

## gui.py
```python
import tkinter as tk
from battle import Battle
from gui_select import SelectScreen
from gui_battle import BattleScreen
# CLASSES = {"Tank": Tank, "Spellcaster": Spellcaster, ...}

# 1. root = tk.Tk(); battle = Battle()
# 2. show SelectScreen(root, CLASSES, on_start)
# 3. on_start(p1_name, p2_name): create CLASSES[p1_name]("P1 " + p1_name) and
#    CLASSES[p2_name]("P2 " + p2_name), call battle.start(p1, p2), swap to BattleScreen(root, battle, on_restart)
# 4. on_restart(): battle.restart(), swap back to SelectScreen
# 5. root.mainloop()
```

## Rules for you
- Others do not edit `character.py` or `battle.py`. If someone asks for a change, decide and tell everyone.
- Merge one branch at a time and run `python -m unittest -v` after each merge.

## Done when
`python gui.py` opens, you can pick two classes, play to a winner, and restart.
