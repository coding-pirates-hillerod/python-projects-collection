groceries = [
    {"item": "Smør", "price": 20},
    {"item": "Mælk", "price": 12},
    {"item": "Brød", "price": 15},
]

total_price = 0

for item in groceries:
    total_price += item["price"]

print(f"Total pris af indkøb: {total_price} kr.")
