import datetime

class Topic:
    def __init__(self, name: str, difficulty: int, time_spent: int, spaced_rep_time: int):
        self.name = name
        self.difficulty = difficulty
        self.time_spent = time_spent
        self.last_done = datetime.datetime.now()
        self.spaced_rep_time = spaced_rep_time
