"""Band Class for CP1404"""


class Band:
    """Band Class."""

    def __init__(self, name=""):
        self.name = name
        self.musicians

    def __str__(self):
        return f"{self.name} ({self.instruments})"
