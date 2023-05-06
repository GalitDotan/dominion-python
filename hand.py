from game_conf.card import Card
from player import Player


class Hand:
    def __init__(self, player: Player, cards: list[Card], revel=False):
        self.player = player
        self.cards = cards

    def revel(self):
        for card in self.cards:
            card.is_reveled = True
