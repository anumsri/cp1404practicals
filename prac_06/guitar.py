"""
CP1404 Practical
Guitar class
"""
CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:
    """Guitar class object"""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get age of guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """sort guitar by year release"""
        return self.year < other.year