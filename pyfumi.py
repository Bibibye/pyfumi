#!/usr/bin/env python3

from game.game import Game
from strats import *

if __name__ == "__main__":
    player_1 = mixed.Mixed()
    player_2 = markov.Markov()
    print(player_1.get_name()+" vs "+player_2.get_name())
    g = Game(player_1, player_2)
    r = g.run_n(1000)
    print("results :"+
          "\n\tDraw : "+str(r.count(0))+
          "\n\t"+player_1.get_name()+" : "+str(r.count(1))+
          "\n\t"+player_2.get_name()+" : "+str(r.count(-1)))
