from OLD.game_conf.card import Action
from OLD.game_conf.command import Command


class Cellar(Action):
    def __init__(self):
        super().__init__(name='Cellar',
                         cost=2,
                         commands=[Command(plus_actions=1),
                                   Command(plus_cards=1)])
