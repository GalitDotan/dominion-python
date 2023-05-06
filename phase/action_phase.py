from hand import Hand
from phase.phase import Phase
from player import Player


class ActionPhase(Phase):
    def __init__(self, player: Player, opponents: list[Player], hand: Hand, actions: int = 1, buys: int = 1):
        super().__init__(player, opponents, hand, actions, buys)
