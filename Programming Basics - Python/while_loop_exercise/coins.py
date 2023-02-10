change = float(input())  # ресто
change_in_coins = round(change * 100)  # рестото в стотинки

coins_number = 0

while change_in_coins > 0:
    if change_in_coins >= 200:
        change_in_coins -= 200
        coins_number += 1
    elif change_in_coins >= 100:
        change_in_coins -= 100
        coins_number += 1
    elif change_in_coins >= 50:
        change_in_coins -= 50
        coins_number += 1
    elif change_in_coins >= 20:
        change_in_coins -= 20
        coins_number += 1
    elif change_in_coins >= 10:
        change_in_coins -= 10
        coins_number += 1
    elif change_in_coins >= 5:
        change_in_coins -= 5
        coins_number += 1
    elif change_in_coins >= 2:
        change_in_coins -= 2
        coins_number += 1
    elif change_in_coins == 1:
        change_in_coins -= 1
        coins_number += 1

print(coins_number)
