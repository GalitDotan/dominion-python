from dominiate.base_cards import province, gold, duchy, estate
from dominiate.basic_ai.basic_ai import buying_value
from dominiate.players.big_money_player import BigMoney


class HillClimbBot(BigMoney):
    def __init__(self, cutoff1=2, cutoff2=3, simulation_steps=100):
        self.simulation_steps = simulation_steps
        if not hasattr(self, 'name'):
            self.name = 'HillClimbBot(%d, %d, %d)' % (cutoff1, cutoff2,
                                                      simulation_steps)
        BigMoney.__init__(self, cutoff1, cutoff2)

    def buy_priority(self, decision, card):
        state = decision.get_game_state()
        total = 0
        if card is None:
            add = ()
        else:
            add = (card,)
        for coins, buys in state.simulate_hands(self.simulation_steps, add):
            total += buying_value(coins, buys)

        # gold is better than it seems
        if card == gold: total += self.simulation_steps / 2
        self.log.debug("%s: %s" % (card, total))
        return total

    def make_buy_decision(self, decision):
        choices = decision.choices()
        provinces_left = decision.game.card_counts[province]

        if province in choices: return province
        if duchy in choices and provinces_left <= self.cutoff2:
            return duchy
        if estate in choices and provinces_left <= self.cutoff1:
            return estate
        return BigMoney.make_buy_decision(self, decision)
