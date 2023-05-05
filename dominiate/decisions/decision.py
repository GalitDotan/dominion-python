from dominiate.game import Game


class Decision(object):
    def __init__(self, game: Game):
        self.game = game

    def get_game_state(self):
        return self.game.curr_player_state()

    def get_curr_player(self):
        return self.game.current_player()
