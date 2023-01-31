actor_name = input()
points_from_academy = float(input())
number_jurries = int(input())
total_points = points_from_academy

for jurry in range(number_jurries):
    current_jurry_name = input()
    point_from_current_jurry = float(input())

    total_points_from_current_jurry = (len(current_jurry_name) * point_from_current_jurry) / 2
    total_points += total_points_from_current_jurry

    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break

if total_points < 1250.5:
    needed_points = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
