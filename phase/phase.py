from hand import Hand
from player import Player


class Phase:
    def __init__(self, player: Player, opponents: list[Player], hand: Hand, actions: int, buys: int):
        self.actions = actions
        self.buys = buys
        self.hand = hand
        self.player = player
        self.vp = 0
        self.opponents = opponents

    def finish(self):
        return self.actions, self.buys, self.vp
