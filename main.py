import user
import model

if __name__ == '__main__':
    
    names = ['Andrzej', 'Blazej', 'Marzenka']
    users = [user.User(name) for name in names]
    
    points_updates = [10, -10, 128]
    for usr, p_update in zip(users, points_updates):
        usr.update_points(p_update)
        
    model = model.Model(users, sort=True)
    
    model.show_ranking()
    
    names2 = ['Karol', 'Jarek', 'Dominika']
    points_updates = [1, 2, -30]
    
    users = [user.User(name) for name in names2]
    for usr, p_update in zip(users, points_updates):
        usr.update_points(p_update)
        
    model.add_users(users, sort=True)
    print('='*50)
    model.show_ranking()
    
    user = user.User('Filip')
    user.update_points(28.3)
    model.add_users(user, sort=True)
    print('='*50)
    model.show_ranking()