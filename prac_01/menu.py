name = input("Enter name: ")

choice = ''
while choice.upper() != 'Q':
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ")

    if choice.upper() == 'H':
        print(f"Hello {name}")
    elif choice.upper() == 'G':
        print(f"Goodbye {name}")
    elif choice.upper() != 'Q':
        print("Invalid choice")

print("Finished.")
