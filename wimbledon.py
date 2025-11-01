"""
CP1404 Practical
Wimbledon data analysis
"""

FILENAME = "wimbledon.csv"


def main():
    """Read Wimbledon data and display champions and countries."""
    records = load_data(FILENAME)
    champion_to_wins, countries = process_data(records)
    display_results(champion_to_wins, countries)


def load_data(filename):
    """Read the data file and return a list of records (each record is a list)."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header
        records = [line.strip().split(",") for line in in_file]
    return records

def process_data(records):
    """Process Wimbledon data into champion win counts and a set of countries."""
    champion_to_wins = {}
    countries = set()
    for record in records:
        if len(record) < 3:  # Skip incomplete or empty rows
            continue
        champion = record[2]
        country = record[1]
        countries.add(country)
        if champion in champion_to_wins:
            champion_to_wins[champion] += 1
        else:
            champion_to_wins[champion] = 1
    return champion_to_wins, countries


def display_results(champion_to_wins, countries):
    """Display the champions with their win counts and the list of countries."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion:20} {wins}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
