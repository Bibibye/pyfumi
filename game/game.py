from game.value import Value

class Game(object):
    valid_plays = ['R','P','S']

    def __init__(self, strat1, strat2):
        self.strat1 = strat1
        self.strat2 = strat2

    def run(self):
        p1 = self.strat1.play()
        p2 = self.strat2.play()
        if p1 not in Game.valid_plays:
            raise ValueError(self.strat1.get_name+" played "+p1)
        if p2 not in Game.valid_plays:
            raise ValueError(self.strat2.get_name+" played "+p2)
        self.strat1.update(p2)
        self.strat2.update(p1)
        return Value.get_value(p1,p2)

    def run_n(self, n):
        results = []
        for i in range(n):
            results.append(self.run())
        return results
