import datetime


class Topic:
    def __init__(self, name: str, difficulty: int, time_spent: int):
        self.name = name
        self.difficulty = difficulty
        self.time_spent = time_spent
        self.last_done = datetime.datetime.now()
        self.is_done = False
