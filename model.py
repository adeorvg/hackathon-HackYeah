import user

class Model:
    
    def __init__(self, users, sort=False):
        self.users = users
        self.ranking = user.Ranking(users, sort)
        
    def add_users(self, users, sort=False):
        try:
            self.users.extend(users)
            for u in users:
                self.ranking.add_user(u)
        except TypeError:
            self.users.append(users)
            self.ranking.add_user(users)
            
        if sort:
            self.ranking.sort_users()
            
    def show_ranking(self):
        self.ranking.show()
            