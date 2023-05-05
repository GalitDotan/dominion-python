from dominiate.decisions.multi_decision import MultiDecision


class DiscardDecision(MultiDecision):
    def choices(self):
        return sorted(list(self.get_game_state().hand))

    def choose(self, choices):
        self.game.log.info("%s discards %s" % (self.get_curr_player().name, choices))
        state = self.get_game_state()
        for card in choices:
            state = state.discard_card(card)
        return self.game.replace_current_state(state)

    def __str__(self):
        return "DiscardDecision" + str(self.get_game_state().hand)
