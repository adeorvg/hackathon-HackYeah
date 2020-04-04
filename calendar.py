import category
import datetime
import topic
import timeblock


class Calendar:
    def __init__(self):
        self.days = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": [],
                     "saturday": [], "sunday": []}
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.block_duration = 25
        self.categories = {}

    def add_event(self, segment, day: str):
        self.days[day].append(segment)

    def set_time_range(self, start, end):
        self.start_time = start
        self.end_time = end

    def set_block_duration(self, duration):
        self.block_duration = duration

    def add_category(self, c: category.Category, time_to_spend: int):
        self.categories[c] = time_to_spend

    def get_block_time_division_coefficient(self, tpc: topic.Topic):
        time = tpc.time_spent
        if time > self.block_duration:
            return time / self.block_duration

    @staticmethod
    def create_time_block(duration, c: category.Category, t=None):
        if t:
            name = c.name + ' / ' + t.name
        else:
            name = c.name
        return timeblock.TimeBlock(name, duration)

    def divide_topic(self, c: category.Category, t: topic.Topic, div_coef):
        small_segment = []
        while div_coef > 0:
            if div_coef >= 1:
                tb = self.create_time_block(t.time_spent, c, t)
                small_segment.append(tb)
                div_coef -= 1
            else:
                tb = self.create_time_block(t.time_spent * div_coef, c, t)
                small_segment.append(tb)
                div_coef -= div_coef
        return small_segment

    def create_segment(self, date_now):
        segment = []
        for c, duration in self.categories:
            topics = c.get_topics(duration)
            for t in topics:
                coef = self.get_block_time_division_coefficient(t)
                small_segment = self.divide_topic(c, t, coef)
                segment.extend(small_segment)
        return segment
