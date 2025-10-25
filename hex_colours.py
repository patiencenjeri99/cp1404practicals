"""
CP1404 Practical
Hexadecimal colour lookup
"""

COLOUR_TO_CODE = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff",
    "BlueViolet": "#8a2be2"
}

def main():
    """Allow user to look up hex colour codes by name."""
    colour_name = input("Enter colour name: ").title()
    while colour_name != "":
        try:
            print(f"The code for {colour_name} is {COLOUR_TO_CODE[colour_name]}")
        except KeyError:
            print("Invalid colour name.")
        colour_name = input("Enter colour name: ").title()


main()
