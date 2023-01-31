number_groups = int(input())

people_climbing_musala = 0
people_climbing_monblan = 0
people_climbing_kilimandzaro = 0
people_climbing_k2 = 0
people_climbing_everest = 0

for current_group in range(number_groups):
    number_people_in_current_group = int(input())

    if number_people_in_current_group <= 5:
        people_climbing_musala += number_people_in_current_group
    elif 6 <= number_people_in_current_group <= 12:
        people_climbing_monblan += number_people_in_current_group
    elif 13 <= number_people_in_current_group <= 25:
        people_climbing_kilimandzaro += number_people_in_current_group
    elif 26 <= number_people_in_current_group <= 40:
        people_climbing_k2 += number_people_in_current_group
    elif number_people_in_current_group >= 41:
        people_climbing_everest += number_people_in_current_group

total_people = people_climbing_musala + people_climbing_monblan + \
               people_climbing_kilimandzaro + people_climbing_k2 \
               + people_climbing_everest

musala_percentage = people_climbing_musala / total_people * 100
monblan_percentage = people_climbing_monblan / total_people * 100
kilimandzaro_percentage = people_climbing_kilimandzaro / total_people * 100
k2_percentage = people_climbing_k2 / total_people * 100
everest_percentage = people_climbing_everest / total_people * 100

print(f"{musala_percentage:.2f}%")
print(f"{monblan_percentage:.2f}%")
print(f"{kilimandzaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")
