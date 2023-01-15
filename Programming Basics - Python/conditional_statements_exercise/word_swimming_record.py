current_world_record = float(input())
distance = float(input())
time_per_meter = float(input())

total_time = distance * time_per_meter
delay = distance // 15 * 12.5

total_time = total_time + delay

if total_time < current_world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    difference = total_time - current_world_record
    print(f"No, he failed! He was {difference:.2f} seconds slower.")

