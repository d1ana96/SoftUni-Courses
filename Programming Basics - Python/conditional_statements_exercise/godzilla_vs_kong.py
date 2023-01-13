film_budget = float(input())
number_people = int(input())
price_for_clothes_per_person = float(input())

decor_price = film_budget * 0.1

if number_people > 150:
    price_for_clothes_per_person = price_for_clothes_per_person - (price_for_clothes_per_person * 0.1)

price_for_all_clothes = number_people * price_for_clothes_per_person

total_price = price_for_all_clothes + decor_price

difference = abs(total_price - film_budget)

if total_price > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
