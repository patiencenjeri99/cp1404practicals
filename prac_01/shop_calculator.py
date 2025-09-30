number_of_items = int(input("Number of items: "))
total_price = 0

for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

# Apply discount if over $100
if total_price > 100:
    total_price *= 0.9

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
