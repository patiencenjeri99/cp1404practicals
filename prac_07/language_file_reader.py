"""
CP1404 Practical - Language file reader
Estimated time: 20 minutes
Actual time: 20 minutes
"""

from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details and display them."""
    languages = load_languages("languages.csv")
    for language in languages:
        print(language)


def load_languages(filename):
    """Load programming languages from a CSV file into a list of ProgrammingLanguage objects."""
    languages = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # Skip header line
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            name, typing, reflection_str, year_str, pointer_str = line.split(",")

            reflection = reflection_str == "Yes"
            pointer_arithmetic = pointer_str == "Yes"
            year = int(year_str)

            language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
            languages.append(language)
    return languages


if __name__ == "__main__":
    main()
