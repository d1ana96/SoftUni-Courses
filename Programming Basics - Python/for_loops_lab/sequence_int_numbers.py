count_numbers = int(input())
numbers_list = []

for number in range(1, count_numbers+1):
    current_number = int(input())
    numbers_list.append(current_number)

print(f"Max number: {max(numbers_list)}")
print(f"Min number: {min(numbers_list)}")
