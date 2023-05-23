box = list(map(int, input().split()))
capacity_of_the_box = int(input())

counter_racks = 1

current_capacity = capacity_of_the_box

while len(box) > 0:
    current_clothes_volume = box.pop()

    if current_clothes_volume <= current_capacity:
        current_capacity -= current_clothes_volume

    else:
        counter_racks += 1
        current_capacity = capacity_of_the_box
        current_capacity -= current_clothes_volume

print(counter_racks)
