import topic
import datetime
import timeblock


class Category:
    def __init__(self, name: str):
        self.name = name
        self.topics = []
        self.last_done = datetime.datetime.now()

    def sort_by_last_done(self):
        self.topics = sorted(self.topics, reverse=True)

    def add_topic(self, tpc: topic.Topic):
        self.topics.append(tpc)
        self.sort_by_last_done()

    def get_topics(self, time_to_spend: int):
        topics = []
        for t in self.topics:
            if t.is_after_spaced_time():
                # set the five minute range to fit the topic
                if t.time_spent <= (time_to_spend + 5):
                    time_to_spend -= t.time_spent
                    topics.append(topic)
        return topics
