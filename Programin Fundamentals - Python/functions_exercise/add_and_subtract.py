def sum_numbers(number_1, number_2):
    return number_1 + number_2


def subtract(sum, number_3):
    return sum - number_3


def add_and_subtract(first, second, third):
    result_sum_numbers = sum_numbers(first, second)
    result_subtract = subtract(result_sum_numbers, third)
    return result_subtract


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
