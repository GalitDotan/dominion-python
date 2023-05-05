import random

from dominiate.base_cards import estate, get_victory_cards_cnt, duchy, province, copper, silver, gold, get_copper_cnt
from dominiate.card import Card
from dominiate.game import PlayerState, Game


def setup(players, kingdom_cards: tuple[Card] = (), simulated: bool = False, num_kingdom_cards: int = 10) -> Game:
    """
    Set up the game.
    """
    num_of_players = len(players)
    num_of_victory_cards = get_victory_cards_cnt(num_of_players)
    counts = {
        estate: num_of_victory_cards,
        duchy: num_of_victory_cards,
        province: num_of_victory_cards,
        copper: get_copper_cnt(num_of_players),
        silver: 40,
        gold: 30
    }

    for card in kingdom_cards:
        counts[card] = num_kingdom_cards

    player_states = [PlayerState.initial_state(p) for p in players]
    random.shuffle(player_states)
    return Game(player_states, counts, turn=0, simulated=simulated)
