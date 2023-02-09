command = input()
steps_sum = 0

while command != "Going home":
    steps_sum += int(command)
    if steps_sum >= 10000:
        break

    command = input()

if command == "Going home":
    steps_to_home = int(input())
    steps_sum += steps_to_home

difference = abs(10000 - steps_sum)

if steps_sum > 10000:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
