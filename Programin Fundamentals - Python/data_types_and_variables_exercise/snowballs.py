number_made_snowballs = int(input())
current_snowball_value = 0
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for each_snowball in range(1, number_made_snowballs + 1):
    current_weight_of_the_snowball = int(input())
    current_time_needed = int(input())
    current_quality_of_the_snowball = int(input())

    current_snowball_value = (current_weight_of_the_snowball / current_time_needed) ** current_quality_of_the_snowball

    if current_snowball_value > max_value:
        max_weight = current_weight_of_the_snowball
        max_time = current_time_needed
        max_quality = current_quality_of_the_snowball
        max_value = current_snowball_value

print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")

