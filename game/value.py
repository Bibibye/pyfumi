class Value(object):
    str_to_int = {'R': 0,
                  'P': 1,
                  'S': 2}

    values = [[0,-1,1],
              [1,0,-1],
              [-1,1,0]]

    def get_value(player_1, player_2):
        p1 = Value.str_to_int[player_1]
        p2 = Value.str_to_int[player_2]
        return Value.values[p1][p2]
