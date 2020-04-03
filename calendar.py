import category


class Calendar:
    def __init__(self):
        self.days = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": []}

    def add_event(self, item: category.Category, day: str):
        self.days[day].append(item)
