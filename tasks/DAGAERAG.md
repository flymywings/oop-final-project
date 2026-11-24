# Dagaerag: Spellcaster + class selection screen

**Files:** `spellcaster.py`, `gui_select.py`

## Checklist
- [ ] `spellcaster.py`: tune the stats and make your own `special_attack` (the starter ignores defense; keep it or change it)
- [ ] `gui_select.py`: the class selection screen (details below)

## spellcaster.py
Keep the class extending `Character`. `special_attack(self, target)` must return a message string. Use `self._deal(...)` to hit; read its options in `character.py`. Spellcaster is the high-POW, low-HEA glass cannon.

## gui_select.py
Write a Tkinter frame with this exact signature so it plugs into `gui.py`:

```python
class SelectScreen(tk.Frame):
    def __init__(self, parent, classes, on_start):
        # classes: dict like {"Tank": Tank, "Spellcaster": Spellcaster, ...}
        # on_start: function you call with two names, e.g. on_start("Tank", "Assassin")
```

- Two columns: **Player 1** and **Player 2**. Each shows one button (or radio button) per class name in `classes`.
- Show which class each player has picked (highlight or a label).
- A **Start** button, disabled until both players have picked. Clicking it calls `on_start(p1_name, p2_name)`.
- You can test it alone with a tiny script that passes `print` as `on_start`.

## Git
```text
git clone https://github.com/flymywings/oop-final-project
cd oop-final-project
git checkout -b dagaerag
# edit only your files, then:
python -m unittest -v
git add spellcaster.py gui_select.py
git commit -m "Spellcaster and selection screen"
git push -u origin dagaerag
```

## Done when
Pushed by **Tuesday night**, finished by **Wednesday noon**.
