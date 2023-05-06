from abc import ABC, abstractmethod


@ABC
class Command:
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class PlusActionsCommand(Command):
    def __init__(self, plus_actions=0):
        self.plus_actions = plus_actions


class DiscardCommand(Command):
    def __init__(self, cards_to_discard_range: tuple[int, int] = (0, float('inf')),
                 reward: Command or None = None):
        self.discard_range = cards_to_discard_range
        self.reward = reward

    def __repr__(self):
        if self.discard_range == (0, float('inf')):
            num = 'any number of'
        elif self.discard_range[0] == self.discard_range[1]:
            num = str(self.discard_range[0])
        else:
            num = f'from {self.discard_range[0]} to {self.discard_range[1]}'

        if self.reward:
            return f"Discard {num} cards, then {str(self.reward)}"
