capacity_of_the_tank = 255
number_lines = int(input())
poured_litters = 0

for current_line in range(number_lines):
    current_litters = int(input())
    if capacity_of_the_tank - current_litters < 0:
        print("Insufficient capacity!")
        continue
    capacity_of_the_tank -= current_litters
    poured_litters += current_litters
print(poured_litters)