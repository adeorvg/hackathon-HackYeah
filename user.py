import calendar
from datetime import datetime

class User:
    def __init__(self, name: str, start_time: datetime, end_time: datetime):
        self.name = name
        self.points = 0
        self.calendar = calendar
        self.friendlist = []
        
        self.start_time = start_time
        self.end_time = end_time

    def update_points(self, pts: int):
        self.points += pts
        
    def add_to_friends(self, users):
        try:
            self.friendlist.extend(users)
        except TypeError:
            self.friendlist.append(users)

class Ranking:
    def __init__(self, users, sort=False):
        self.users = []
        try:
            self.users.extend(users)
        except TypeError:
            self.users = [users]
            
        if sort:
            self.sort_users()
        
    def add_user(self, user):
        self.users.append(user)
        
    def sort_users(self):
        self.users.sort(key=lambda x: x.points, reverse=True)
        
    def show(self):
        for user in self.users:
            print(user.name, ' points:', user.points)