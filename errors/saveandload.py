class NoGameSaved(Exception):
    def __init__(self, message="Error loading game. No games saved."):
        self.message = message
        super().__init__(self.message)

class CantSaveGame(Exception):
    def __init__(self, message="Error saving game. Check logs to see more detail."):
        self.message = message
        super().__init__(self.message)