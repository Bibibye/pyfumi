#!/usr/bin/env python3

from game.game import Game
from strats.dummy import Dummy
from strats.markov import Markov
from strats.mixed import Mixed
from strats.human import Human

def duel(player_1, player_2, nb_games=1000):
    print(player_1.get_name()+" vs "+player_2.get_name())
    g = Game(player_1, player_2)
    r = g.run_n(nb_games)
    print("results :"+
          "\n\tDraw : "+str(r.count(0))+
          "\n\t"+player_1.get_name()+" : "+str(r.count(1))+
          "\n\t"+player_2.get_name()+" : "+str(r.count(-1)))

def hline():
    print("-"*80)

if __name__ == "__main__":
    print("Test Mixed")
    duel(Dummy("R"), Mixed())
    duel(Dummy("RRRPPSP"), Mixed())
    hline()

    print("Test Markov(1)")
    duel(Dummy("R"), Markov(1))
    duel(Dummy("RRRPPSP"), Markov(1))
    hline()

    print("Test Markov(2)")
    duel(Dummy("R"), Markov(2))
    duel(Dummy("RRRPPSP"), Markov(2))
