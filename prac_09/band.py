"""Band Class for CP1404"""


class Band:
    """Band Class."""

    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        musician_strings = []
        for musician in self.musicians:
            musician_strings.append(str(musician))
        return f"{self.name} ({', '.join(musician_strings)})"

    def add(self, musician):
        self.musicians.append(musician)
