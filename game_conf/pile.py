import random
from copy import deepcopy
from typing import Type

from game_conf.card import Card


def generate_card_pile(card: Card, cnt: int or None = None):
    """
    Generate a pile of this card.
    """
    cnt_in_pile = card.default_pile_size if cnt is None else cnt
    cards = [deepcopy(card) for _ in range(cnt_in_pile)]
    return Pile(cards)


class Pile:
    """A pile of cards."""

    def __init__(self, cards: list[Card] = None, name: str = 'Pile', top_reveled: bool = True, shuffle: bool = False):
        self.cards: list[Card] = [] if cards is None else cards  # cards[0] is the top
        if shuffle:
            self.shuffle()
        self.name = name
        self.top_reveled = top_reveled

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return str((self.top.name, len(self)))

    def shuffle(self):
        """shuffle all cards in pile"""
        random.shuffle(self.cards)

    def empty(self):
        return len(self) == 0

    @property
    def top(self):
        if not self.top_reveled or self.empty():
            return None
        return self.cards[0]

    def draw(self, count: int = 1):
        """
        Draw number of cards.

        :param count: number of cards to draw
        :return: a card or list of drawn cards, int the drawn order: first drawn would be in index 0.
        """
        if count == 1:
            self.cards.pop(0)
        cards = []
        for i in range(count):
            cards.append(self.cards.pop(0))
        return cards

    def append(self, card: Card):
        self.cards.append(card)

    def put_on_top(self, card: Card):
        self.cards.insert(0, card)
