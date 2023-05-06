from abc import ABC, abstractmethod
from copy import deepcopy

from game_conf.command import Command


class Card(ABC):
    """
    A card in a game. Stats can be modified
    """

    def __init__(self, name: str, cost: int, vp: int = 0, default_pile_size=10, is_reveled=False):
        self.name: str = name
        self.cost: int = cost
        self.vp: int = vp
        self.default_pile_size = default_pile_size
        self.is_reveled = is_reveled

    def __repr__(self):
        return f"""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ### {self.name} ###
        
        # Type: {self.type}
        # Cost: {self.cost}
        
        {self.description}
        
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """

    def __lt__(self, other: 'Card'):
        if self.cost < other.cost:
            return True
        if self.cost > other.cost:
            return False
        return self.name < other.name

    @property
    def type(self):
        types = [t for t in CARD_TYPES if type(self) is t]
        if len(types) == 1:
            return str(types[0])
        return ' - '.join([str(t) for t in types])

    @abstractmethod
    def play(self):
        raise NotImplementedError()


class Action(Card):

    def __init__(self, name: str, cost: int, commands: list[Command]):
        super().__init__(name, cost)
        self.commands: list[Command] = commands

    @property
    def description(self):
        return "\n".join([str(c) for c in self.commands])

    def play(self) -> list[Command]:
        return deepcopy(self.commands)


class Treasure(Card):

    def __init__(self, name: str, cost: int, coins: int):
        super().__init__(name, cost)
        self.coins = coins

    def __repr__(self):
        return f"""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ### {self.name} ###

        # Type: {self.type}
        # Cost: {self.cost}

        ~ {self.coins} ~

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """

    def play(self):
        return self.coins


class Curse(Card):
    def __init__(self, vp=-1, *args, **kwargs):
        super().__init__(vp=vp, *args, **kwargs)

    def __repr__(self):
        return f"""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ### Curse ###

        # Type: {self.type}
        # Cost: {self.cost}

        ~ {self.vp} VP ~

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """


class Victory(Card):

    def __init__(self, name, cost, vp, *args, **kwargs):
        super().__init__(name=name, cost=cost, vp=vp, *args, **kwargs)

    def __repr__(self):
        return f"""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ### {self.name} ###

        # Type: {self.type}
        # Cost: {self.cost}

        ~ {self.vp} VP ~

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """

    def play(self):
        pass


class Reaction(Card):
    pass


class Attack(Card):
    pass


CARD_TYPES = (Action, Treasure, Curse, Reaction, Attack)