import numpy as np


def deck_value(deck):
    return sum([card.cost for card in deck]) - len(deck)
