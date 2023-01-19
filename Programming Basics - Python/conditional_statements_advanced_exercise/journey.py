budget = float(input())
season = input()
destination = ""
place = ""
spent_money = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent_money = budget * 0.3
        place = "Camp"
    elif season == "winter":
        spent_money = budget * 0.7
        place = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent_money = budget * 0.4
        place = "Camp"
    elif season == "winter":
        spent_money = budget * 0.8
        place = "Hotel"
elif budget > 1000:
    destination = "Europe"
    spent_money = budget * 0.9
    place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {spent_money:.2f}")