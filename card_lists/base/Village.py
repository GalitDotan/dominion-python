from game_conf.card import Action


class Village(Action):
    def __init__(self):
        super().__init__(name='Village',
                         cost=3,
                         plus_cards=2,
                         plus_actions=1)
