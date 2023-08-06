"""Band Class for CP1404"""


class Band:
    """Band Class."""

    def __init__(self, name=""):
        """Initialise a Band object"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of Band."""
        musician_strings = []
        for musician in self.musicians:
            musician_strings.append(str(musician))
        return f"{self.name} ({', '.join(musician_strings)})"

    def add(self, musician):
        """Add Musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Return string showing musician playing their instrument."""
        return "\n".join(musician.play() for musician in self.musicians)

