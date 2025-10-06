# exceptions_demo.py

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Questions:
# 1. ValueError occurs when non-numeric input is entered.
# 2. ZeroDivisionError occurs when denominator = 0.
# 3. To avoid ZeroDivisionError, check denominator != 0 before dividing.
