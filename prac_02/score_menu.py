"""Menu-driven score program with functions."""

import random


def main():
    """Display menu for score operations."""
    score = get_valid_score()  # start with a valid score
    MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_result(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell! Thanks for using the program.")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def determine_result(score):
    """Determine result string based on the given score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print as many stars as the score value."""
    print("*" * int(score))


main()
