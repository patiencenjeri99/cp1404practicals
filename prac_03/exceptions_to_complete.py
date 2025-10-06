# exceptions_to_complete.py

finished = False
result = 0
while not finished:
    try:
        number = int(input("Please enter a number: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print(f"Your number is: {number}")
