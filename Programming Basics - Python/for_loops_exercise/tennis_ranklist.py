from math import floor
number_tournaments = int(input())
initial_points = int(input())
total_points = 0
won_tournaments = 0

for tournament in range(number_tournaments):
    finish_state = input()

    if finish_state == "W":
        total_points += 2000
        won_tournaments += 1
    elif finish_state == "F":
        total_points += 1200
    elif finish_state == "SF":
        total_points += 720

final_points = total_points + initial_points
average_won_points = floor(total_points / number_tournaments)
percentage_won_tournaments = (won_tournaments / number_tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_won_points}")
print(f"{percentage_won_tournaments:.2f}%")
