class Decision(object):
    def __init__(self, game):
        self.game = game

    def state(self):
        return self.game.state()

    def player(self):
        return self.game.current_player()
