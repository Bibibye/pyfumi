from strats.strat import Strat
from random import randrange

class Mixed(Strat):
    def __init__(self):
        self.name = "mixed"

    def play(self):
        choice = ['R','P','S']
        return choice[randrange(len(choice))]

    def update(self, opponent_last_play):
        pass
