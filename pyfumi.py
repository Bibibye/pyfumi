#!/usr/bin/env python3

from game.game import Game
from strats import *

if __name__ == "__main__":
    player_1 = human.Human()
    player_2 = mixed.Mixed()
    print(player_1.get_name()+" vs "+player_2.get_name())
    g = Game(player_1, player_2)
    r = g.run_n(5)
    print(r)
