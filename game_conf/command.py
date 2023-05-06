class Command:
    def __init__(self, plus_actions=0, plus_buys=0, plus_vp=0, plus_cards=0):
        self.plus_actions = plus_actions
        self.plus_buys = plus_buys
        self.plus_vp = plus_vp
        self.plus_cards = plus_cards

    def __repr__(self):
        return "a nice description"  # TODO: the action's description
