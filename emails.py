"""
CP1404 Practical
Emails and names stored in a dictionary
"""


def main():
    """Store emails and corresponding names in a dictionary."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ('', 'y', 'yes'):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from the email before the '@' and format it properly."""
    name_part = email.split('@')[0]
    name = " ".join(name_part.split('.')).title()
    return name


main()
