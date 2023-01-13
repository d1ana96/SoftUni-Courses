import math

series_name = input()
time_of_episode = int(input())
time_of_break = int(input())

time_for_lunch = time_of_break / 8
time_for_rest = time_of_break / 4

needed_time = time_of_episode + time_for_rest + time_for_lunch
left_time = abs(time_of_break - needed_time)

if needed_time <= time_of_break:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(left_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(left_time)} more minutes.")
