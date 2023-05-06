import random
from copy import deepcopy

from card_lists.base.Copper import Copper
from card_lists.base.Estate import Estate
from game_conf.card import Card
from game_conf.pile import Pile, generate_card_pile
from mat.trash import Trash
from player import Player
from user import User


class Table:
    def __init__(self, users: list[User], conf: 'TableConf'):
        self._users = deepcopy(users)
        random.shuffle(self._users)
        self.players: list[Player] = [Player(name=user.username,
                                             cards=conf.generate_start_cards_player()) for user in self._users]
        self.turn_number = 1
        self.conf = conf
        self.kingdom_cards = conf
        self.supply_piles = conf.generate_supply_piles()
        self.trash = Trash()

    @property
    def supply(self) -> str:
        return "\r\n".join([str(s) for s in self.supply_piles])

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
        {self.supply}
        #######################################################
        """


class TableConf:
    """
    This class represents a game table.
    It stores all the necessary configuration for running a Dominion game.
    """

    def __init__(self, cards_level_range: tuple[int, int] = (1, 10),
                 num_supply_range: tuple[int, int] = (10, 10), card_conf: dict[Card, int] = None):
        self._cards_level_range = cards_level_range
        self.kingdom_cards_range: tuple[int, int] = num_supply_range

        self.card_conf = card_conf
        if card_conf is None:
            self.card_conf = {
                Copper: 7,
                Estate: 3
            }

    @property
    def allowed_cards(self) -> list[Card]:
        """
        Calculating from allowed expansions, player's cards lists etc.
        """
        return []

    def generate_supply_piles(self) -> list[Pile]:
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

    def generate_start_cards_player(self) -> list[Card]:
        """
        Generate a list of new cards a player receives in the beginning of the game.
        """
        cards = []
        for card_type, cnt in self.card_conf.items():
            cards.extend([card_type() for _ in range(cnt)])
        return cards
