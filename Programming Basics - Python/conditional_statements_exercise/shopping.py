budget = float(input())
number_videocards = int(input())
number_core = int(input())
number_ram = int(input())

videocard_price = number_videocards * 250
core_price = (videocard_price * 0.35) * number_core
ram_price = (videocard_price * 0.1) * number_ram

final_price = videocard_price + core_price + ram_price

if number_videocards > number_core:
    final_price = final_price - (final_price * 0.15)

if budget >= final_price:
    left_budget = budget - final_price
    print(f"You have {left_budget:.2f} leva left!")
else:
    needed_budget = abs(final_price - budget)
    print(f"Not enough money! You need {needed_budget:.2f} leva more!")
