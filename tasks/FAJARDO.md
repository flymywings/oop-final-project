# Fajardo: Marksman + tests

**Files:** `marksman.py`, `test_battle.py`

## Checklist
- [ ] `marksman.py`: tune the stats and make your own `special_attack` (the starter is two quick shots)
- [ ] `test_battle.py`: add tests so the rubric concepts are proven (list below)

## marksman.py
Keep the class extending `Character`. `special_attack(self, target)` must return a message string. Use `self._deal(...)` to hit; read its options in `character.py`. Marksman is the balanced ranged fighter.

## Tests to add (there are 5 already; keep them passing)
- Each class has the right five attributes and `max_hp == hea * 10`.
- `take_damage` never drops HP below 0, and `heal` never goes above max HP.
- A normal attack always does at least 1 damage.
- A character with 0 dodge and 0 luck takes predictable damage (use `random.seed(...)`, or build a test class with fixed stats).
- `Battle.play` with a bad action name does nothing.
- Nobody can act after a winner is decided (`play` returns `None`).
- Polymorphism: loop all five classes and call `special_attack`; each returns a string.

Run with `python -m unittest -v`. All tests must pass before anyone merges.

## Git
```text
git clone https://github.com/flymywings/oop-final-project
cd oop-final-project
git checkout -b fajardo
# edit only your files, then:
python -m unittest -v
git add marksman.py test_battle.py
git commit -m "Marksman and tests"
git push -u origin fajardo
```

## Done when
Pushed by **Tuesday night**, finished by **Wednesday noon**.
