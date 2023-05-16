from collections import deque

liters = int(input())
name = input()
line = deque()

while name != "Start":
    line.append(name)
    name = input()

command = input()

while command != "End":
    if command.isdigit():
        required_liters = int(command)
        name = line.popleft()
        if liters >= required_liters:
            liters -= required_liters
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    else:
        _, liters_to_fill = command.split()
        liters_to_refill = int(liters_to_fill)
        liters += liters_to_refill
    command = input()
print(f"{liters} liters left")
