"""
CP1404 Practical - More Guitars program
Estimated time: 20 minutes
Actual time: 25 minutes
"""

from guitar import Guitar


FILENAME = "guitars.csv"


def main():
    """Read guitars from a file, display them, allow adding new ones, then save."""
    guitars = load_guitars(FILENAME)
    print("These are my guitars:")
    display_guitars(guitars)

    print("\nAdd new guitars:")
    guitars = add_new_guitars(guitars)

    guitars.sort()
    print("\nSorted guitars:")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print(f"\nGuitars saved to {FILENAME}")


def load_guitars(filename):
    """Load guitars from a CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars nicely formatted."""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
              f"worth ${guitar.cost:10,.2f}{vintage_string}")


def add_new_guitars(guitars):
    """Ask user for guitars to add and append them to the list."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")
    return guitars


def save_guitars(filename, guitars):
    """Save the list of guitars back to the CSV file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
