list_of_numbers = input().split()

opposite_numbers_list = list()

for element in list_of_numbers:
    current_element = -int(element)
    opposite_numbers_list.append(current_element)
print(opposite_numbers_list)