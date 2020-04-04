import topic
import datetime


class Category:
    def __init__(self, name: str):
        self.name = name
        self.topics = []
        self.last_done = datetime.datetime.now()

    def add_topic(self, tpc: topic.Topic):
        self.topics.append(tpc)
