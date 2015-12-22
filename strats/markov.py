from strats.strat import Strat
from random import randrange

class Markov(Strat):
    def __init__(self, n=1):
        if n < 1:
            raise ValueError("n must be greater than 1")
        self.name = "markov"
        self.n = n
        self.mem = 'X'*n
        self.strat = {}
        self.nb_plays = 0

    def play(self):
        try:
            choose_from = self.strat[self.mem]
            return choose_from[randrange(len(choose_from))]
        except KeyError:
            choice = ['R','P','S']
            return choice[randrange(len(choice))]

    def update(self, opponent_last_play):
        win = {'R':'P',
               'P':'S',
               'S':'R'}
        if not 'X' in self.mem:
            if self.mem in self.strat:
                self.strat[self.mem].append(win[opponent_last_play])
            else:
                self.strat[self.mem] = [win[opponent_last_play]]
        self.mem = self.mem[1:]+opponent_last_play
