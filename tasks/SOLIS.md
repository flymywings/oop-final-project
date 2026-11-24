# Solis: Warrior + report and slides

**Files:** `warrior.py`, `REPORT.md`

## Checklist
- [ ] `warrior.py`: tune the stats and make your own `special_attack` (the starter is a 2x hit with recoil)
- [ ] `REPORT.md`: explain how the project shows the four rubric concepts (below)
- [ ] Slides or talking points for Thursday, one person per section

## warrior.py
Keep the class extending `Character`. `special_attack(self, target)` must return a message string. Use `self._deal(...)` to hit; read its options in `character.py`. Warrior is the all-rounder.

## REPORT.md
For each concept, write 3-4 simple sentences and name the file and the exact line or method:
1. **Encapsulation**: private `_pow`, `_hp`, etc. in `character.py`, read through `@property`; `hp` cannot be set from outside.
2. **Abstraction**: `Character(ABC)` and the abstract `special_attack()`; you cannot create a plain `Character`.
3. **Inheritance**: five classes extending `Character` and reusing `attack`, `heavy_attack`, `_deal`.
4. **Polymorphism**: each class overrides `special_attack()`; `battle.py` calls `getattr(attacker, action)(defender)` without knowing the class.

Also list: the five attributes and what each does, the five classes and what makes each different, and the damage formulas (see the README).

Then agree with the group who presents which section on Thursday.

## Git
```text
git clone https://github.com/flymywings/oop-final-project
cd oop-final-project
git checkout -b solis
# edit only your files, then:
python -m unittest -v
git add warrior.py REPORT.md
git commit -m "Warrior and report"
git push -u origin solis
```

## Done when
Warrior pushed by **Tuesday night**, report finished by **Wednesday night** (it needs the final code).
