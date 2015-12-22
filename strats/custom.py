from strats.strat import Strat
from random import random

class Custom(Strat):
    def __init__(self, R=1/3, P=1/3, S=1/3):
        self.R = R
        self.P = P
        self.S = S
        if self.R+self.P+self.S != 1:
            raise ValueError
        self.name = "custom("+str(self.R)+","+str(self.P)+","+str(self.S)+")"

    def play(self):
        r = random()
        if r < self.R:
            return 'R'
        elif r < self.R+self.P:
            return 'P'
        else:
            return 'S'

    def update(self, opponent_last_play):
        pass
