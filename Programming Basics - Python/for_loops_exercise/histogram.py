count_numbers = int(input())

count_numbers_for_percentage_1 = 0
count_numbers_for_percentage_2 = 0
count_numbers_for_percentage_3 = 0
count_numbers_for_percentage_4 = 0
count_numbers_for_percentage_5 = 0

for number in range(count_numbers):
    current_number = int(input())
    if current_number < 200:
        count_numbers_for_percentage_1 += 1
    elif 200 <= current_number <= 399:
        count_numbers_for_percentage_2 += 1
    elif 400 <= current_number <= 599:
        count_numbers_for_percentage_3 += 1
    elif 600 <= current_number <= 799:
        count_numbers_for_percentage_4 += 1
    elif current_number >= 800:
        count_numbers_for_percentage_5 += 1

percentage_1 = count_numbers_for_percentage_1 / count_numbers * 100
percentage_2 = count_numbers_for_percentage_2 / count_numbers * 100
percentage_3 = count_numbers_for_percentage_3 / count_numbers * 100
percentage_4 = count_numbers_for_percentage_4 / count_numbers * 100
percentage_5 = count_numbers_for_percentage_5 / count_numbers * 100

print(f"{percentage_1:.2f}%")
print(f"{percentage_2:.2f}%")
print(f"{percentage_3:.2f}%")
print(f"{percentage_4:.2f}%")
print(f"{percentage_5:.2f}%")


