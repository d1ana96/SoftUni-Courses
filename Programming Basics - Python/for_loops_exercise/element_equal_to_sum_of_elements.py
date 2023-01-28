import sys
count_numbers = int(input())
sum_numbers = 0
max_number = - sys.maxsize

for number in range(count_numbers):
    current_number = int(input())
    sum_numbers += current_number
    if current_number > max_number:
        max_number = current_number

if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    sum_numbers = sum_numbers - max_number
    difference = abs(max_number - sum_numbers)
    print("No")
    print(f"Diff = {difference}")
