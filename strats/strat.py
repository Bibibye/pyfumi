class Strat(object):
    def play(self):
        raise NotImplementedError()

    def update(self, opponent_last_play):
        raise NotImplementedError()

    def get_name(self):
        return "no name" if not self.name else self.name
