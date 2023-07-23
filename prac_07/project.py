"""
CP1404/CP5632 Practical - Project Management Program
ESTIMATE: 1:30hr
ACTUAL:
"""


class Project:
    def __init__(self, name, start_date, cost_estimate, completion_rate, priority):
        self.name = name
        self.start_date = start_date
        self.cost_estimate = cost_estimate
        self.completion_rate = completion_rate
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, " \
               f"completion: {self.completion_rate}%"
