from dominiate.base_cards import silver, gold, province
from dominiate.basic_ai.combo_bot.idealist_combo_bot import IdealistComboBot
from dominiate.players.big_money_player import BigMoney


class ComboBot(IdealistComboBot):
    def buy_priority_order(self, decision):
        if self.strategy_complete:
            return BigMoney.buy_priority_order(self, decision)
        else:
            return [None, silver] + self.strategy_priority + [gold, province]
