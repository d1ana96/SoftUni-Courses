main_points = int(input())
bonus_points = 0
if main_points <= 100:
    bonus_points = 5
elif main_points > 1000:
    bonus_points = main_points * 0.1
else:
    bonus_points = main_points * 0.2

total_bonus = 0
if main_points % 2 == 0:
    total_bonus = bonus_points + 1
elif main_points % 10 == 5:
    total_bonus = bonus_points + 2
else:
    total_bonus = bonus_points

total_points = main_points + total_bonus

print(total_bonus)
print(total_points)
