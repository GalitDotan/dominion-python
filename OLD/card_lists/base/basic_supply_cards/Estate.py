from OLD.game_conf.card import Victory


class Estate(Victory):
    def __init__(self):
        super().__init__(name='Estate', cost=2, vp=1)
