from retry import retry

from dominiate.game import INF
from dominiate.decisions.multi_decision import MultiDecision
from dominiate.players.big_money_player import BigMoney
from dominiate.players.player import Player


class HumanPlayer(Player):
    def __init__(self, name):
        self.name = name

    def make_decision(self, decision):
        if decision.game.simulated:
            # Don't ask the player to tell the AI what they'll do!
            return self.substitute_ai().make_decision(decision)
        state = decision.game.get_game_state()
        print(state.hand)
        print("Deck: %d cards" % state.deck_size())
        print("VP: %d" % state.score())
        print(decision)
        if isinstance(decision, MultiDecision):
            chosen = self.make_multi_decision(decision)
        else:
            chosen = self.make_single_decision(decision)
        return decision.choose(chosen)

    @retry(exceptions=(ValueError, IndexError), tries=5)
    def make_single_decision(self, decision):
        choices = decision.choices()
        for index, choice in enumerate(choices):
            print("\t[%d] %s" % (index, choice))
        choice_index = int(input('Your choice: '))
        print(f"You chose {choice_index}")
        return choices[choice_index]

    def make_multi_decision(self, decision):
        for index, choice in enumerate(decision.choices()):
            print("\t[%d] %s" % (index, choice))
        if decision.min != 0:
            print("Choose at least %d options." % decision.min)
        if decision.max != INF:
            print("Choose at most %d options." % decision.max)
        choices = input('Your choices (separated by commas): ')
        try:
            chosen = [decision.choices()[int(choice.strip())]
                      for choice in choices.split(',')]
            return chosen
        except (ValueError, IndexError):
            # Try again
            print("That's not a valid list of choices.")
            return self.make_multi_decision(decision)
        if len(chosen) < decision.min:
            print("You didn't choose enough things.")
            return self.make_multi_decision(decision)
        if len(chosen) > decision.max:
            print("You chose too many things.")
            return self.make_multi_decision(decision)
        for ch in chosen:
            if chosen.count(ch) > 1:
                print("You can't choose the same thing twice.")
                return self.make_multi_decision(decision)

    def substitute_ai(self):
        return BigMoney()
