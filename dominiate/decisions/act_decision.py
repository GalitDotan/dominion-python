from dominiate.decisions.decision import Decision


class ActDecision(Decision):
    def choices(self):
        return [None] + [card for card in self.get_game_state().hand if card.isAction()]

    def choose(self, card):
        self.game.log.info("%s plays %s" % (self.get_curr_player().name, card))
        if card is None:
            newgame = self.game.change_current_state(
                delta_actions=-self.get_game_state().actions
            )
            return newgame
        else:
            newgame = card.perform_action(self.game.current_play_action(card))
            return newgame

    def __str__(self):
        return "ActDecision (%d actions, %d buys, +%d coins)" % \
            (self.get_game_state().actions, self.get_game_state().buys, self.get_game_state().coins)
