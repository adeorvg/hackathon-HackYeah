import datetime

class Topic:
    def __init__(self, name: str, difficulty: int, time_spent: int):
        self.name = name
        self.difficulty = difficulty
        self.time_spent = time_spent
        self.last_done = datetime.datetime.now()
<<<<<<< HEAD
        
=======
        self.is_done = False
>>>>>>> 7119289242643d3b4387e767dc6a8e02f561bb4c
