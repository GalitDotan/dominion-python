from game_conf.card import Card


class Mat:
    def __init__(self, cards: list[Card] = None):
        self.cards = [] if cards is None else cards

    def view_cards(self):
        """View all the cards on the mat."""
        return self.cards

    def put(self, cards: list[Card]):
        """Put cards on the mat"""
        self.cards.extend(cards)

    def gain(self, name: str):
        return self.cards.remove(name)
