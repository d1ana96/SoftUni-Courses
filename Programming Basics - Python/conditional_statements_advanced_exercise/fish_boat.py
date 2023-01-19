budget = int(input())
season = input()
number_fishers = int(input())

price = 0
mid_price = 0

if season == "Spring":
    price = 3000
    if number_fishers <= 6:
        mid_price = price - (price * 0.1)
    elif 7 <= number_fishers <= 11:
        mid_price = price - (price * 0.15)
    elif number_fishers >= 12:
        mid_price = price - (price * 0.25)
elif season == "Summer" or season == "Autumn":
    price = 4200
    if number_fishers <= 6:
        mid_price = price - (price * 0.1)
    elif 7 <= number_fishers <= 11:
        mid_price = price - (price * 0.15)
    elif number_fishers >= 12:
        mid_price = price - (price * 0.25)
elif season == "Winter":
    price = 2600
    if number_fishers <= 6:
        mid_price = price - (price * 0.1)
    elif 7 <= number_fishers <= 11:
        mid_price = price - (price * 0.15)
    elif number_fishers >= 12:
        mid_price = price - (price * 0.25)


additional_discount = 0
if number_fishers % 2 == 0:
    if season != "Autumn":
        additional_discount = mid_price * 0.95


final_price = mid_price - additional_discount

difference = abs(budget - final_price)

if final_price <= budget:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")