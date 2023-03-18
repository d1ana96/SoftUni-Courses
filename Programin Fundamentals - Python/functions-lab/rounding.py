main_list = input().split()
final_list = []

for element in main_list:
    current_number = round(float(element))
    final_list.append(current_number)
print(final_list)
