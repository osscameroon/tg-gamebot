# This class represents the game entity that users interact with on Telegram while using this bot

class Game:
    def __init__(self, name, difficulty, players, duration, description):
        self.name = name
        self.difficulty = difficulty
        self.players = players
        self.duration = duration
        self.description = description

    
