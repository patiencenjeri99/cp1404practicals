numbers = [1, 2, 3, 4, 5, 6]

# Example:
squares = [n ** 2 for n in numbers]
print(squares)

evens = [n for n in numbers if n % 2 == 0]
print(evens)

doubled = [n * 2 for n in numbers]
print(doubled)

# Filter strings longer than 3 characters
names = ["Bob", "Sally", "Tom", "Elizabeth", "Jo"]
long_names = [name for name in names if len(name) > 3]
print(long_names)

# Convert all names to lowercase
lowercase_names = [name.lower() for name in names]
print(lowercase_names)
