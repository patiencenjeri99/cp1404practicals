"""Example output"""
name = "Gibson L-5 CES"
year = 1922
cost = 16035.999

# Using f-string formatting
print(f"{year} {name} for about ${cost:,.0f}!")

# Using a for loop to print powers of 2 (aligned neatly)
for i in range(11):
    print(f"2 ^ {i:2} is {2 ** i:4}")
