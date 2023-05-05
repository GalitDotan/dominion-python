from dominiate.card import Card

# define the cards that are in every game
curse = Card('Curse', 0, vp=-1)
estate = Card('Estate', 2, vp=1)
duchy = Card('Duchy', 5, vp=3)
province = Card('Province', 8, vp=6)
copper = Card('Copper', 0, treasure=1)
silver = Card('Silver', 3, treasure=2)
gold = Card('Gold', 6, treasure=3)

# How many duchies/provinces are there for n players?
_V_CARDS_BY_PLAYER_CNT = {
    1: 5,  # useful for simulation
    2: 8,
    3: 12,
    4: 12,
    5: 15,
    6: 18
}


def get_victory_cards_cnt(num_of_players: int):
    """
    How many duchies/provinces are there for n players?
    """
    return _V_CARDS_BY_PLAYER_CNT[num_of_players]


def get_copper_cnt(num_of_players: int):
    return 60 - 7 * num_of_players
