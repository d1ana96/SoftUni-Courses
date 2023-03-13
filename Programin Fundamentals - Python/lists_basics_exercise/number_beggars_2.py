list_of_given_money = input().split(", ")
number_of_beggars = int(input())

money_list = []
for current_element in list_of_given_money:
    money_list.append(int(current_element))

final_list_of_sums = []

starting_index = 0


while starting_index < number_of_beggars:
    sum_for_current_beggar = 0
    for current_index in range(starting_index, len(money_list), number_of_beggars):
        sum_for_current_beggar += money_list[current_index]
    final_list_of_sums.append(sum_for_current_beggar)
    starting_index += 1

print(final_list_of_sums)