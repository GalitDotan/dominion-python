from enum import Enum


class ExpansionName(Enum):
    DEPRECATED = -1
    PROMOS = 0
    BASE = 1
    INTRIGUE = 2
    SEA_SIDE = 3
    ALCHEMY = 4
    PROSPERITY = 5
    CORNUCOPIA = 6
    HINTERLANDS = 7
    DARK_AGES = 8
    GUILDS = 9
    ADVENTURES = 10
    EMPIRES = 11
    NOCTURNE = 12
    RENAISSANCE = 12
    MENAGERIE = 13
    ALLIES = 14
    PLUNDER = 15


class Expansion:
    def __init__(self, kingdom_cards_configs):
        pass
