"""Password check program with functions."""

def main():
    """Get password and print stars."""
    password = get_password()
    print_stars(password)


def get_password():
    """Get a valid password from user and return it."""
    MIN_LENGTH = 5
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter password: ")
    return password


def print_stars(password):
    """Print stars equal to password length."""
    print("*" * len(password))


main()
