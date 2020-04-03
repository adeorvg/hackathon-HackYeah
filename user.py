import calendar


class User:
    def __init__(self, name: str):
        self.name = name
        self.points = 0
        self.calendar = calendar

    def update_points(self, pts: int):
        self.points += pts
