days = int(input())
type_room = input()
feedback = input()

price = 0
nights = days - 1

if type_room == "room for one person":
    price = 18.00 * nights

elif type_room == "apartment":
    price = 25.00 * nights
    if days < 10:
        price -= price * 0.3
    elif 10 <= days <= 15:
        price -= price * 0.35
    elif days > 15:
        price -= price * 0.5

elif type_room == "president apartment":
    price = 35.00 * nights
    if days < 10:
        price -= price * 0.1
    elif 10 <= days <= 15:
        price -= price * 0.15
    elif days > 15:
        price -= price * 0.2

if feedback == "positive":
    price += price * 0.25
elif feedback == "negative":
    price -= price * 0.1

print(f"{price:.2f}")
