from dominiate.decisions.decision import Decision
from dominiate.game import INF


class MultiDecision(Decision):
    def __init__(self, game, min=0, max=INF):
        self.min = min
        self.max = max
        Decision.__init__(self, game)
