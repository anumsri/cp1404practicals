"""
CP1404 Practical
Read guitar file program
"""
FILENAME = "guitars.csv"


class Guitar:
    """Represent guitar class"""
    def __init__(self, name, year, cost):
        """Initialise object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        """"Comparison based on year"""
        return self.year < other.year


def main():
    """Read data, sort and display function"""
    guitars = get_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)


def get_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            year = int(year)
            cost = float(cost)
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display the guitar details nicely"""
    for guitar in guitars:
        print(f"{guitar.name}, {guitar.year}, ${guitar.cost:.2f}")


main()
