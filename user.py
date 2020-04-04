import calendar
from datetime import datetime
import category


class User:
    def __init__(self, name: str, ):
        self.name = name
        self.points = 0
        self.calendar = calendar
        self.friend_list = []

    def update_points(self, pts: int):
        self.points += pts
        
    def add_to_friends(self, users):
        try:
            self.friend_list.extend(users)
        except TypeError:
            self.friend_list.append(users)



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
