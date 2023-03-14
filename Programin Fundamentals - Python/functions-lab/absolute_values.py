numbers_list = input().split()
abs_list = []

for element in numbers_list:
    current_number = abs(float(element))
    abs_list.append(current_number)
print(abs_list)
