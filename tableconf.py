import random
from copy import deepcopy

from card_lists.base.Copper import Copper
from card_lists.base.Estate import Estate
from game_conf.card import Card
from game_conf.pile import Pile, generate_card_pile
from player import Player
from user import User


class Table:
    def __init__(self, users: list[User], conf: 'TableConf'):
        self._users = deepcopy(users)
        random.shuffle(self._users)
        self.players: list[Player] = [user.get_player() for user in self._users]
        self.turn_number = 1
        self.conf = conf
        self.kingdom_cards = conf
        self.suply_piles = conf.generate_suply_piles()
        self.trash = []  # TODO: implement trash

    @property
    def suply(self) -> str:
        return "\r\n".join([str(s) for s in self.suply_piles])

    @property
    def curr_player_index(self) -> int:
        return (self.turn_number - 1) % len(self.players)

    @property
    def curr_player(self) -> Player:
        return self.players[self.curr_player_index]

    def __repr__(self):
        return f"""
        #######################################################
                        # The Table #
                        
        # Players: {self.players}
        # Current player: {self.curr_player.name}
        
        # Suply:
        {self.suply}
        #######################################################
        """


class TableConf:
    """
    This class represents a game table.
    It stores all the necessary configuration for running a Dominion game.
    """

    def __init__(self, cards_level_range: tuple[int, int] = (1, 10),
                 num_suply_range: tuple[int, int] = (10, 10)):
        self._cards_level_range = cards_level_range
        self.kingdom_cards_range: tuple[int, int] = num_suply_range

    @property
    def allowed_cards(self) -> list[Card]:
        """
        Calculating from allowed expansions, player's cards lists etc.
        """
        return []

    def generate_suply_piles(self) -> list[Pile]:
        allowed_cards = self.allowed_cards
        total = random.randint(self.kingdom_cards_range[0], self.kingdom_cards_range[1])
        piles = []
        for i in range(total):
            card: Card = random.choice(allowed_cards)
            allowed_cards.remove(card)  # TODO: should remove all cards with the same name
            piles.append(generate_card_pile(card))

        piles.append(generate_card_pile(Copper()))
        piles.append(generate_card_pile(Estate()))
        return piles
