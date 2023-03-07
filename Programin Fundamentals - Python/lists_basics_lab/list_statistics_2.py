count_of_numbers = int(input())
list_positive_numbers = []
list_negative_numbers = []
sum_of_negatives = 0

for number in range(count_of_numbers):
    current_number = int(input())
    if current_number >= 0:
        list_positive_numbers.append(current_number)
    elif current_number < 0:
        list_negative_numbers.append(current_number)
        sum_of_negatives += current_number

print(list_positive_numbers)
print(list_negative_numbers)
print(f"Count of positives: {len(list_positive_numbers)}")
print(f"Sum of negatives: {sum_of_negatives}")


