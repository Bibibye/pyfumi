from game.game import Game
from strats import *

if __name__ == "__main__":
    player_1 = dummy.Dummy()
    player_2 = human.Human()
    print(player_1.get_name()+" vs "+player_2.get_name())
    g = Game(player_1, player_2)
    r = g.run_n(5)
    print(r)
