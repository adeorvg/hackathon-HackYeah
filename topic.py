import datetime


class Topic:
    def __init__(self, name: str, difficulty: int):
        self.name = name
        self.difficulty = difficulty
        self.last_done = datetime.datetime.now()
        self.is_done = False

