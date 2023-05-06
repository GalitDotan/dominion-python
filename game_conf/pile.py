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

    def __init__(self, cards: list[Card], name='Pile', is_top_reveled=True):
        self.cards: list[Card] = cards  # cards[0] is the top
        self.name = name
        self.top_reveled = is_top_reveled

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return str((self.top.name, len(self)))

    def empty(self):
        return len(self) == 0

    @property
    def top(self):
        if not self.top_reveled or self.empty():
            return None
        return self.cards[0]

    def draw(self):
        self.cards.pop(0)

    def append(self, card: Card):
        self.cards.append(card)

    def put_on_top(self, card: Card):
        self.cards.insert(0, card)
