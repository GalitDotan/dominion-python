from game_conf.card import Card


class Hand:
    def __init__(self, cards: list[Card], revel=False):
        self.cards = cards

    def revel(self):
        for card in self.cards:
            card.is_reveled = True
