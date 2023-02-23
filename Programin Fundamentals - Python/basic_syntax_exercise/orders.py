number_of_orders = int(input())
total_price = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    amount_capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif amount_capsules_per_day < 1 or amount_capsules_per_day > 2000:
        continue
    price_for_coffee = price_per_capsule * (days * amount_capsules_per_day)
    print(f"The price for the coffee is: ${price_for_coffee:.2f}")
    total_price += price_for_coffee

print(f"Total: ${total_price:.2f}")