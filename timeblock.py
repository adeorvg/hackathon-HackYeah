import datetime


class TimeBlock:
    def __init__(self, name: str, duration=5):
        self.name = name
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.is_done = False
        self.duration = duration
        
    def finish_block(self):
        self.is_done = True

    def set_time_range(self, start_time):
        self.start_time = start_time
        self.end_time = self.start_time + datetime.timedelta(minutes=self.duration)
