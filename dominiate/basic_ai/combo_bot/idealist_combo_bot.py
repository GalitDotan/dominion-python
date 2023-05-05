import numpy as np

from dominiate import cards as c
from dominiate.basic_ai.combo_bot.utils import deck_value
from dominiate.game import Game
from dominiate.setup_game import setup
from dominiate.players.big_money_player import BigMoney

# precalculated; easier than loading a pickle or something
BASELINE = np.array(
    [1.8226, 1.8302, 2.4849, 2.5363, 3.2383, 3.6883, 3.9152, 4.4961,
     4.5271, 4.8773, 4.9464, 4.9591, 5.0117, 5.2145, 5.2473, 5.2609,
     5.1505, 5.1500, 5.2662, 5.4229]
)


class IdealistComboBot(BigMoney):
    def __init__(self, strategy, name=None):
        self.strategy = strategy
        self.strategy_on = True
        self.strategy_complete = False
        if name is None:
            self.name = 'IdealistComboBot(%s)' % (strategy)
        else:
            self.name = name
        BigMoney.__init__(self, 1, 2)

    def before_turn(self, game):
        current_cards = game.get_game_state().all_cards()
        priority = []
        needed = {}
        pending = False
        for card, round in self.strategy:
            if card not in needed: needed[card] = 0
            if round <= game.round:
                needed[card] += 1
            else:
                pending = True
        for card in needed:
            needed[card] -= current_cards.count(card)
            if needed[card] > 0: priority.append(card)

        priority.sort(key=lambda card: (needed[card], card.cost))
        self.strategy_priority = priority
        self.log.debug('Strategy: %s' % self.strategy_priority)
        self.strategy_on = bool(priority)
        self.strategy_complete = not (priority or pending)

    def buy_priority_order(self, decision):
        if self.strategy_complete:
            return BigMoney.buy_priority_order(self, decision)
        else:
            return [None, c.silver, c.gold, c.province] + self.strategy_priority

    def make_buy_decision(self, decision):
        choices = decision.choices()
        choices.sort(key=lambda x: self.buy_priority(decision, x))
        return choices[-1]

    def test(self):
        improvements = np.zeros((30,))
        counts = np.zeros((30,), dtype='int32')
        for iteration in range(100):
            game = setup(c.variable_cards, simulated=False)
            turn_count = 0
            # Find a state where the strategy is done and the deck is
            # about to be shuffled
            while not (game.card_counts[c.province] <= 1 or
                       (game.current_player().strategy_complete and
                        len(game.get_game_state().drawpile) < 5)):
                game = game.take_turn()
                turn_count += 1
                assert game.round == turn_count
            if turn_count <= 18:
                for trial in range(10):
                    # take one more turn to shuffle the deck
                    game1 = game.take_turn()
                    # test the next turn
                    before_value = deck_value(game1.get_game_state().all_cards())
                    game2 = game1.take_turn()
                    after_value = deck_value(game2.get_game_state().all_cards())
                    improvements[turn_count + 1] += \
                        (after_value - before_value - BASELINE[turn_count + 1])
                    counts[turn_count + 1] += 1
            avg = improvements / counts
            overall = np.sum(improvements) / np.sum(counts)
            self.log.info(str(overall))
            self.log.info('\n%s' % avg)
        self.log.info('Overall gain: %s' % overall)
        return overall
