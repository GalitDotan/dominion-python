from dominiate.decisions.multi_decision import MultiDecision


class TrashDecision(MultiDecision):
    def choices(self):
        return sorted(list(self.state().hand))

    def choose(self, choices):
        self.game.log.info("%s trashes %s" % (self.player().name, choices))
        state = self.state()
        for card in choices:
            state = state.trash_card(card)
        return self.game.replace_current_state(state)

    def __str__(self):
        return "TrashDecision(%s, %s, %s)" % (self.state().hand, self.min, self.max)
