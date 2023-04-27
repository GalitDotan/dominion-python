from dominiate.decisions.decision import Decision


class ActDecision(Decision):
    def choices(self):
        return [None] + [card for card in self.state().hand if card.isAction()]

    def choose(self, card):
        self.game.log.info("%s plays %s" % (self.player().name, card))
        if card is None:
            newgame = self.game.change_current_state(
                delta_actions=-self.state().actions
            )
            return newgame
        else:
            newgame = card.perform_action(self.game.current_play_action(card))
            return newgame

    def __str__(self):
        return "ActDecision (%d actions, %d buys, +%d coins)" % \
            (self.state().actions, self.state().buys, self.state().coins)
