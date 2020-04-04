import datetime

GMT_OFF = "+02:00"

class TimeBlock:
    def __init__(self, name: str, duration=5):
        self.name = name
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.is_done = False
        self.duration = duration
        
    def finish(self):
        self.is_done = True

    def set_time_range(self, start_time):
        self.start_time = start_time
        self.end_time = self.start_time + datetime.timedelta(minutes=self.duration)

    def to_google_calendar(self):
        ##GMT_OFF = "+01:00"
        return {
            "summary": self.name,
            "start": {"dateTime": (self.start_time.strftime("%Y-%m-%dT%H:%M:00") + "%s") % GMT_OFF},
            "end":  {"dateTime": (self.end_time.strftime("%Y-%m-%dT%H:%M:00") + "%s") % GMT_OFF}
        }
