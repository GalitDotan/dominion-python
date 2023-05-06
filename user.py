from player import Player


class User:
    def __init__(self, name, is_bot=False):
        self.username = name
        self.card_lists = []
        self.is_bot = is_bot
        self.liked_cards = []
        self.disliked_cards = []
        self.banned_cards = []

    def get_player(self):
        return Player(name=self.username,
                      is_bot=self.is_bot)