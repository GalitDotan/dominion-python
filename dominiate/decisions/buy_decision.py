from dominiate.decisions.decision import Decision


class BuyDecision(Decision):
    def coins(self):
        return self.state().hand_value()

    def buys(self):
        return self.state().buys

    def choices(self):
        assert self.coins() >= 0
        value = self.coins()
        return [None] + [card for card in self.game.card_choices() if card.cost <= value]

    def choose(self, card):
        self.game.log.info("%s buys %s" % (self.player().name, card))
        state = self.state()
        if card is None:
            newgame = self.game.change_current_state(
                delta_buys=-state.buys
            )
            return newgame
        else:
            newgame = self.game.remove_card(card).replace_current_state(
                state.gain(card).change(delta_buys=-1, delta_coins=-card.cost)
            )
            return newgame

    def __str__(self):
        return "BuyDecision (%d buys, %d coins)" % \
            (self.buys(), self.coins())
