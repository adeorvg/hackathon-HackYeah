import datetime

class TimeBlock:
    
    def __init__(self, name: str, start_time: datetime.datetime, end_time: datetime.datetime):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        
        self.is_done = False
        
    def end_block(self):
        self.is_done = True