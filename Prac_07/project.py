import datetime


class Project:
    def __init__(self, name, date, priority, cost, completion):
        self.name = name
        self.date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __repr__(self):
        return f"{self.name},{self.date.strftime('%d/%m/%y ')},{self.priority},{self.cost},{self.completion}"

    def __str__(self):
        return f"{self.name}, start: {self.date.strftime('%d/%m/%y')}, priority: {self.priority}, estimate: ${self.cost}," \
               f" completion: {self.completion}%"

    def __lt__(self, other):
        return int(self.priority) < int(other.priority)

    def is_complete(self):
        return int(self.completion) == 100

    def is_after_date(self, cutoff_date):
        return self.date > cutoff_date
