"""
CP1404/CP5632 Practical -
Wimbledon data-reading
Estimate: 40 minutes
Actual:   1hr:20 minutes
"""
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read file and print details"""
    data = get_data(FILENAME)
    champion_counts, countries = process_data(data)
    display_results(champion_counts, countries)


def process_data(data):
    """process collection of data items"""
    champion_count = {}
    countries = set()
    for item in data:
        countries.add(item[INDEX_COUNTRY])
        try:
            champion_count[item[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_count[item[INDEX_CHAMPION]] = 1
    return champion_count, countries


def get_data(filename):
    """retrieve data and format correctly for processing"""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
    return data


def display_results(champion_to_count, countries):
    """Display champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()