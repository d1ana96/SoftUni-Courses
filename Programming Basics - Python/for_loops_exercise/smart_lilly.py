current_years = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

money_for_current_birthday = 0
money_for_all_birthdays = 0
number_toys = 0
money_for_brother = 0
total_money = 0

for birthday in range(1, current_years + 1):
    if birthday % 2 == 0:
        money_for_current_birthday += 10
        money_for_all_birthdays += money_for_current_birthday
        money_for_brother += 1

    elif birthday % 2 != 0:
        number_toys += 1

total_price_for_toys = number_toys * price_per_toy
total_money = total_price_for_toys + money_for_all_birthdays - money_for_brother

difference = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")


