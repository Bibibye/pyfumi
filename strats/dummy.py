from strats.strat import Strat

class Dummy(Strat):
    def __init__(self, choice='R'):
        self.choice = choice
        self.name = "dummy"

    def play(self):
        return self.choice

    def update(self, opponent_last_play):
        pass

