trip_price = float(input())
number_puzzles = int(input())
number_talking_dolls = int(input())
number_teddy_bear = int(input())
number_minions = int(input())
number_trucks = int(input())

all_number_toys = number_puzzles + number_talking_dolls + number_teddy_bear + number_minions + number_trucks

discount = 0

first_earned_money = number_puzzles * 2.60 + number_talking_dolls * 3 + number_teddy_bear * 4.10 + number_minions * 8.20 + number_trucks * 2

if all_number_toys >= 50:
    discount = first_earned_money * 0.25

total_earned_money = first_earned_money - discount

loan = total_earned_money * 0.1

left_money = total_earned_money - loan
difference = abs(left_money - trip_price)


if left_money >= trip_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")

