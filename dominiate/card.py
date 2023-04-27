class Card(object):
    """
    Represents a class of card.

    To save computation, only one of each card should be constructed. Decks can
    contain many references to the same Card object.
    """

    def __init__(self, name, cost, treasure=0, vp=0, coins=0, cards=0,
                 actions=0, buys=0, potionCost=0, effect=(), isAttack=False,
                 isDefense=False, reaction=(), duration=()):
        self.name = name
        self.cost = cost
        self.potionCost = potionCost
        if isinstance(treasure, int):
            self.treasure = treasure
        else:
            self.treasure = property(treasure)
        if isinstance(vp, int):
            self.vp = vp
        else:
            self.vp = property(vp)
        self.coins = coins
        self.cards = cards
        self.actions = actions
        self.buys = buys
        self._isAttack = isAttack
        self._isDefense = isDefense
        if not isinstance(effect, (tuple, list)):
            self.effect = (effect,)
        else:
            self.effect = effect
        self.reaction = reaction
        self.duration = duration

    def __lt__(self, other:'Card'):
        if self.cost < other.cost:
            return True
        if self.cost > other.cost:
            return False
        return self.name < other.name

    def isVictory(self):
        return self.vp > 0

    def isCurse(self):
        return self.vp < 0

    def isTreasure(self):
        return self.treasure > 0

    def isAction(self):
        return (self.coins or self.cards or self.actions or self.buys or
                self.effect)

    def isAttack(self):
        return self._isAttack

    def isDefense(self):
        return self._isDefense

    def perform_action(self, game):
        assert self.isAction()
        if self.cards:
            game = game.current_draw_cards(self.cards)
        if (self.coins or self.actions or self.buys):
            game = game.change_current_state(
                delta_coins=self.coins,
                delta_actions=self.actions,
                delta_buys=self.buys
            )
        for action in self.effect:
            game = action(game)
        return game

    def __str__(self):
        return self.name

    def __cmp__(self, other):
        if other is None: return -1
        return cmp((self.cost, self.name),
                   (other.cost, other.name))

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name
