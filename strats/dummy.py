from strats.strat import Strat

class Dummy(Strat):
    def __init__(self, choice=['R']):
        self.choice = choice
        self.name = "dummy"
        self.count = 0
        self.frequency = len(choice)

    def play(self):
        choice = self.choice[self.count%self.frequency]
        self.count += 1
        return choice

    def update(self, opponent_last_play):
        pass

