from dominiate.decisions.multi_decision import MultiDecision


class TrashDecision(MultiDecision):
    def choices(self):
        return sorted(list(self.get_game_state().hand))

    def choose(self, choices):
        self.game.log.info("%s trashes %s" % (self.get_curr_player().name, choices))
        state = self.get_game_state()
        for card in choices:
            state = state.trash_card(card)
        return self.game.replace_current_state(state)

    def __str__(self):
        return "TrashDecision(%s, %s, %s)" % (self.get_game_state().hand, self.min, self.max)
