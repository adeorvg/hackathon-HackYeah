from abc import ABC, abstractmethod
import json
import datetime
from . import user
from . import category
from . import topic
from . import calendar

class View(ABC):
    
    def __init__(self, controller=None):
        self.controller = controller
        
    def add_controller(self, controller):
        self.controller = controller
    
    @abstractmethod
    def show_ranking():
        pass
    
    @abstractmethod
    def send_callendar():
        pass
    
class DemoView(View):
    
    def __init__(self, controller=None):
        View.__init__(self, controller)
        self.ranking_descending = True
        
    def show_ranking(self):
        self.controller.show_ranking(self.ranking_descending)
        
    def sort_ranking(self, is_descending=True):
        self.ranking_descending = False
        
    def send_callendar(self):
        # send to Google Calendar
        self.controller.send_callendar()
            
    def launch(self, file):
        """
        Launches a program that simulate user's inputs

        Parameters:
            file(str): name of the file from which categories and topics are being loaded
        """
        self.controller.read_categories_and_topics(file)
        
        new_calendar = calendar.Calendar()

        new_calendar.set_time_range(new_calendar.start_time, new_calendar.start_time + datetime.timedelta(hours=8))
        categories = self.controller.get_categories()
        times = [300, 300]
        for new_category, time in zip(categories, times):
            new_calendar.add_category(new_category, time)
        new_calendar.create(n_days=5)
        
        self.controller.set_calendar(new_calendar)
        self.send_callendar()
        
    
class Model:
    
    def __init__(self, u, calendar=None, sort=True):
        self.user = u
        self.ranking = user.Ranking(u)
        for friend in u.friend_list:
            self.ranking.add_user(friend)
        if sort:
            self.ranking.sort_users()
            
        self.calendar = calendar
        self.categories = []
        
class Controller(ABC):
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    @abstractmethod
    def add_friend():
        pass
            
    @abstractmethod
    def get_ranking():
        pass
    
    @abstractmethod
    def add_category():
        pass
    
    @abstractmethod
    def get_category():
        pass
        
class DemoController(Controller):
    
    def __init__(self, model, view):
        Controller.__init__(self, model, view)
        
    def add_friend(self, u, sort=False):
        """
        Add friend for the current user.

        Parameters:
            u(user.User): reference for user that the current user wants to add to friends.
            sort(bool): boolean that decides whether to sort the friend list by points or not.
        """
        self.model.user.add_friend(u)
        self.model.ranking.add_user(u)
            
        if sort:
            self.model.ranking.sort_users()
            
    def get_ranking(self):
        return self.model.ranking
        
    def add_category(self, category):
        self.model.categories.append(category)
        
    def get_category(self, name):
        """
        Add category for the current user.

        Parameters:
            name(str): name of the category.
        """
        
        categories = self.model.categories
        
        for concrete_category in categories:
            if concrete_category.name == name:
                return concrete_category
            
        return category.Category(name)
    
    def get_categories(self):
        return self.model.categories
    
    def set_calendar(self, calendar):
        self.model.calendar = calendar
        
    def add_category_to_calendar(self, new_category):
        self.model.calendar.add_category(new_category)
        
    def send_calendar(self):
        self.model.calendar.add_to_google()
        
    def send_callendar(self):
        # send to Google Calendar
        self.model.calendar.add_to_google()
        
    def read_categories_and_topics(self, file):
        """
        Read categories and topics from .json file.

        Parameters:
            file(str): name of the json file.
        """
        with open(file, 'r') as fp:
            d = json.load(fp)
            
        for category_name in d.keys():
            new_category = category.Category(category_name)
            
            for topic_name, values in zip(d[category_name].keys(), d[category_name].values()):
                new_topic = topic.Topic(name=topic_name, difficulty=values[0], time_spent=values[1])
                new_category.add_topic(new_topic)
                
            self.add_category(new_category)
            