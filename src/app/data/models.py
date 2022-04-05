# This class represents the game entity that users interact with on Telegram while using this bot

class Game:
    def __init__(self, name, difficulty, players, duration, description):
        self.name = name
        self.difficulty = difficulty
        self.players = players
        self.duration = duration
        self.description = description


class Player:
    def __init__(self, username, score, time):
        self.username = username
        self.score = score
        self.time = time


# All the game models

# The Quiz Game
class Quiz(Game):
    def __init__(self, name, difficulty, players, duration, description, questions):
        super().__init__(name, difficulty, players, duration, description)
        self.questions = questions