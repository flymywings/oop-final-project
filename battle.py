"""Turn-based battle rules. Owner: Sean (Collado).

The Battle only calls attack / heavy_attack / special_attack on a Character.
It never checks which class it is, so any new class works (polymorphism).
"""


class Battle:
    ACTIONS = ("attack", "heavy_attack", "special_attack")

    def __init__(self):
        self.restart()

    def restart(self):
        self.player1 = None
        self.player2 = None
        self.current_turn = None   # 1 or 2; None before a match and after a win
        self.winner = None
        self.log = []

    def start(self, player1, player2):
        self.restart()
        self.player1 = player1
        self.player2 = player2
        self.current_turn = 1

    def play(self, action):
        """Run one action ('attack', 'heavy_attack', 'special_attack') for the current player."""
        if self.current_turn is None or action not in self.ACTIONS:
            return None
        attacker, defender = (
            (self.player1, self.player2) if self.current_turn == 1
            else (self.player2, self.player1)
        )
        message = getattr(attacker, action)(defender)
        self.log.append(message)
        if not defender.is_alive():
            self.winner = attacker
            self.current_turn = None
            self.log.append(f"{attacker.name} wins!")
        elif not attacker.is_alive():      # e.g. Warrior recoil
            self.winner = defender
            self.current_turn = None
            self.log.append(f"{defender.name} wins!")
        else:
            self.current_turn = 2 if self.current_turn == 1 else 1
        return message
