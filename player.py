from game_conf.card import Card, Victory, Curse
from game_conf.pile import Pile
from hand import Hand


class Player:
    def __init__(self, name: str, cards: list[Card], is_bot: bool = False):
        """
        Note: the cards are the actual card instances. Should be unique for each player.
        """
        self._is_bot = is_bot
        self.name = name
        self.is_ready = True if is_bot else False
        self.is_loud = False if is_bot else True

        # Game stats
        self.cards: list[Card] = cards  # all cards the player has
        self.draw_pile: Pile = Pile(cards, name='Draw Pile', top_reveled=False, shuffle=True)
        top_5 = self.draw_pile.draw(5)
        self.hand: Hand = Hand(cards=top_5)
        self.discard_pile: Pile = Pile(name='Discard Pile', top_reveled=True)

    def __repr__(self):
        return self.name

    def readiness(self, is_ready=True):
        """
        Is player ready to start the game?
        """
        self.is_ready = is_ready

    @property
    def vp(self):
        vp = 0
        for c in self.cards:
            if type(c) in (Victory, Curse):
                vp += c.vp
        return vp

    def play_turn(self):
        pass
