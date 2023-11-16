from OLD.game_conf.card import Victory


class Duchy(Victory):
    def __init__(self):
        super().__init__(name='Duchy', cost=5, vp=3)
