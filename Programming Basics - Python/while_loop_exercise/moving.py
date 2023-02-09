width = int(input())
length = int(input())
hight = int(input())

available_room_volume = width * length * hight
no_more_space = False

command = input()
while command != "Done":
    current_box_volume = int(command)
    available_room_volume -= current_box_volume
    if available_room_volume <= 0:
        no_more_space = True
        break
    command = input()

if no_more_space:
    print(f"No more free space! You need {abs(available_room_volume)} Cubic meters more.")
else:
    print(f"{available_room_volume} Cubic meters left.")
