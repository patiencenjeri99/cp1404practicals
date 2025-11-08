"""
CP1404/CP5632 Practical - Guitars(client program)
"""

from prac_06.guitar import Guitar


def main():
    """Store and display details of guitars."""
    guitars = []
    print("My guitars!")

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    # If no input, use these for testing instead of typing each time
    if not guitars:
        guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
        guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
              f"worth ${guitar.cost:10,.2f}{vintage_string}")


main()
