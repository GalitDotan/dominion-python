from OLD.game_conf.card import Treasure


class Silver(Treasure):
    def __init__(self):
        super().__init__(name='Silver', cost=3, coins=2)
