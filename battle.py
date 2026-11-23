class Battle:
    def __init__(self):
        self.restart()

    def start(self, marvel_hero, dc_hero):
        """Start a match with two freshly created heroes."""
        self.marvel_hero = marvel_hero
        self.dc_hero = dc_hero
        self.current_turn = 1
        self.winner = None
        self.log = [f"{marvel_hero.get_name()} vs {dc_hero.get_name()}!"]

    def play(self, action):
        """Apply the active player's action and return whether it was played."""
        if self.current_turn is None:
            return False

        if self.current_turn == 1:
            hero, opponent = self.marvel_hero, self.dc_hero
        else:
            hero, opponent = self.dc_hero, self.marvel_hero

        if action == "attack":
            message = hero.attack(opponent)
        elif action == "skill":
            message = hero.use_skill(opponent)
        elif action == "heal":
            message = hero.heal()
        else:
            return False

        self.log.append(message)
        if opponent.get_health() == 0:
            self.winner = hero
            self.log.append(f"{hero.get_name()} wins!")
            self.current_turn = None
        else:
            self.current_turn = 2 if self.current_turn == 1 else 1
        return True

    def restart(self):
        """Clear the match so the players can pick heroes again."""
        self.marvel_hero = None
        self.dc_hero = None
        self.current_turn = None
        self.winner = None
        self.log = []
