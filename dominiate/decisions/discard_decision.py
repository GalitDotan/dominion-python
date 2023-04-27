from dominiate.decisions.multi_decision import MultiDecision


class DiscardDecision(MultiDecision):
    def choices(self):
        return sorted(list(self.state().hand))

    def choose(self, choices):
        self.game.log.info("%s discards %s" % (self.player().name, choices))
        state = self.state()
        for card in choices:
            state = state.discard_card(card)
        return self.game.replace_current_state(state)

    def __str__(self):
        return "DiscardDecision" + str(self.state().hand)
