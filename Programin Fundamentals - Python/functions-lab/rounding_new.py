def converted_list(main_list):
    final_list = []
    for element in main_list:
        current_number = round((float(element)))
        final_list.append(current_number)
    return final_list


input_list = input().split()

print(converted_list(input_list))

