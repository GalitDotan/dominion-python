class Player(object):
    def __init__(self, *args):
        raise NotImplementedError("Player is an abstract class")

    def make_decision(self, decision, state):
        assert state.player is self
        raise NotImplementedError

    def make_multi_decision(self, decision, state):
        raise NotImplementedError

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Player: %s>" % self.name

    def before_turn(self, game):
        pass

    def after_turn(self, game):
        pass
