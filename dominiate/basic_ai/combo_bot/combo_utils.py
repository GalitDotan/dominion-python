# Thoughts on a combo bot:
# 
# It should probably run the BigMoney strategy by default; it will not work
# for minimalist (Chapel) or maximalist (Garden) strategies.
# 
# A ComboBot aims to get a certain set of cards. It pays an opportunity cost
# in the number of turns it could have been running BigMoney. How do we compare
# this? I think in the average value of cards it gains per turn, plus possibly
# a constant bonus for trashing useless cards.
#
# We're looking for strategies that gain more per turn than BigMoney would
# after being run for the same number of turns.
import logging

import numpy as np

from dominiate import cards as c
from dominiate.basic_ai.combo_bot.combo_bot import ComboBot
from dominiate.basic_ai.combo_bot.utils import deck_value
from dominiate.game import Game
from dominiate.setup_game import setup
from dominiate.players.big_money_player import BigMoney


def big_money_baseline():
    improvements = np.zeros((30,))
    counts = np.zeros((30,), dtype='int32')
    for iteration in range(10000):
        game = setup()
        for turn in range(30):
            before_value = deck_value(game.get_game_state().all_cards())
            game = game.take_turn()
            after_value = deck_value(game.get_game_state().all_cards())
            delta = after_value - before_value
            improvements[turn] += delta
            counts[turn] += 1
            if game.over(): break
        avg = [imp / count for imp, count in zip(improvements, counts)]
        print(avg)
        print(counts)
    return avg


smithyComboBot = ComboBot([(c.smithy, 2), (c.smithy, 6)],
                          name='smithyComboBot')

chapelComboBot = ComboBot([(c.chapel, 0),
                           (c.laboratory, 0),
                           (c.laboratory, 0),
                           (c.laboratory, 0),
                           (c.market, 0),
                           ], name='chapelComboBot')
chapelComboBot2 = ComboBot([(c.chapel, 0), (c.smithy, 2), (c.smithy, 6),
                            (c.festival, 0), (c.festival, 4)],
                           name='chapelComboBot2')

if __name__ == '__main__':
    strategy = chapelComboBot
    strategy.setLogLevel(logging.INFO)
    strategy.test()
