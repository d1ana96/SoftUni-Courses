number = int(input())

list_all_numbers = list()

for i in range(number):
    current_integer = int(input())
    list_all_numbers.append(current_integer)

command = input()
list_filtered = list()

for current_number in list_all_numbers:
    if command == "even" and current_number % 2 == 0:
        list_filtered.append(current_number)
    if command == "odd" and current_number % 2 != 0:
        list_filtered.append(current_number)
    if command == "positive" and current_number >= 0:
        list_filtered.append(current_number)
    if command == "negative" and current_number < 0:
        list_filtered.append(current_number)

print(list_filtered)

