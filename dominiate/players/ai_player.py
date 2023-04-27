import logging

from dominiate.decisions.discard_decision import DiscardDecision
from dominiate.decisions.trash_decision import TrashDecision
from dominiate.decisions.buy_decision import BuyDecision
from dominiate.decisions.act_decision import ActDecision
from dominiate.players.player import Player


class AIPlayer(Player):
    def __init__(self):
        self.log = logging.getLogger(self.name)

    def setLogLevel(self, level):
        self.log.setLevel(level)

    def make_decision(self, decision):
        self.log.debug(f"Decision: {decision}")
        if isinstance(decision, BuyDecision):
            choice = self.make_buy_decision(decision)
        elif isinstance(decision, ActDecision):
            choice = self.make_act_decision(decision)
        elif isinstance(decision, DiscardDecision):
            choice = self.make_discard_decision(decision)
        elif isinstance(decision, TrashDecision):
            choice = self.make_trash_decision(decision)
        else:
            raise NotImplementedError
        return decision.choose(choice)
