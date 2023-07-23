"""
CP1404/CP5632 Practical - Project Management Program
ESTIMATE: 1:30hr
ACTUAL:
"""


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_rate):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_rate = completion_rate

    def __lt__(self, other):
        self.priority = other.year
