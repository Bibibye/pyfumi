from game.value import Value
from strats.strat import Strat

class Human(Strat):
    def __init__(self):
        self.last_play = ''
        self.name = "human"

    def play(self):
        c = ''
        while c not in ['R','P','S']:
            c = input("What do you play ? (R/P/S)").upper()
        self.last_play = c
        return c

    def update(self, opponent_last_play):
        message = ["You lose", "Draw", "You win"]
        print("The opponent plays " + 
              opponent_last_play+
              "\n"+
              message[Value.get_value(self.last_play, opponent_last_play)+1])
