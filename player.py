class Player:
    def __init__(self, name: str, is_bot: bool = False):
        self._is_bot = is_bot
        self.name = name
        self.is_ready = True if is_bot else False
        self.is_loud = False if is_bot else True

    def __repr__(self):
        return self.name

    def readiness(self, is_ready=True):
        self.is_ready = is_ready
