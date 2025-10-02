"""Program to determine score status with functions."""

import random


def main():
    """Get a score from the user and print the result. Then generate a random score."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    # Generate and check a random score
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    print(determine_result(random_score))


def determine_result(score):
    """Determine result string based on the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
