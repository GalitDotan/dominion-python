import random
from collections import defaultdict

from dominiate.basic_ai.combo_bot.combo_utils import *
from .basic_ai.hill_climb_bot import HillClimbBot
from .cards import variable_cards
from .players.human_player import HumanPlayer


def compare_bots(bots):
    scores = defaultdict(int)
    for i in range(50):
        random.shuffle(bots)
        game = Game.setup(bots, variable_cards)
        results = game.run()
        maxscore = 0
        for bot, score in results:
            if score > maxscore: maxscore = score
        for bot, score in results:
            if score == maxscore:
                scores[bot] += 1
                break
    return scores


def test_game():
    player1 = smithyComboBot
    player2 = chapelComboBot
    player3 = HillClimbBot(2, 3, 40)
    player2.setLogLevel(logging.DEBUG)
    game = Game.setup([player1, player2, player3], variable_cards)
    results = game.run()
    return results


def human_game():
    player1 = smithyComboBot
    player2 = chapelComboBot
    player3 = HillClimbBot(2, 3, 40)
    player4 = HumanPlayer('You')
    game = Game.setup([player1, player2, player3, player4], get_rand_cards())
    return game.run()


def get_rand_cards():
    # TODO: choose randomly
    return variable_cards[-10:]
