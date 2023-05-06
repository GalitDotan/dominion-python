from enum import Enum


class Level(Enum):
    ONE = 1, 'base'
    TWO = 2, 'simple'
    THREE = 3, 'duration, special treasures, platinum & colony'
    FOUR = 4, 'when-gained, when-trashed, VP tokens'
    FIVE = 5, 'coffers, villagers, exile, this turn'
    SIX = 6, 'while-in-play, when discard, mats'
    SEVEN = 7, 'events, reserve, adventures tokens'
    EIGHT = 8, 'projects, landmarks, night, shelter, horses'
    NINE = 9, 'extra cards, artifacts, boons, hexes, heirloom'
    TEN = 10, 'all'
