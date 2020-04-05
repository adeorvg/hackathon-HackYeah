import calendar


class User:
    def __init__(self, name: str, ):
        self.name = name
        self.points = 0
        self.calendar = calendar
        self.friend_list = []

    def update_points(self, pts: int):
        """
        Update points of user

        Parameters:
        pts(int): new amount of points
        """
        self.points += pts
        
    def add_friend(self, user):
        self.friend_list.append(user)
            
    def show_friends_ranking(self, sort=True):
        """
        Show your place and points among other friends

        Parameters:
        sort(boolean): alphanumeric sorting
        """
        users = self.friend_list.copy()
        current_user = User('YOU')
        current_user.update_points(self.points)
        
        users.append(current_user)
        ranking = Ranking(users)
        if sort:
            ranking.sort_users()
        ranking.show()

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
        
    def sort_users(self, is_descending=True):
        self.users.sort(key=lambda x: x.points, reverse=is_descending)
        
    def show(self):
        for user in self.users:
            print(user.name, ' points:', user.points)
