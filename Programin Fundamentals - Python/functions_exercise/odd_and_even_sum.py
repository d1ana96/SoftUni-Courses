def sum_even_and_odd(digits):
    even_sum = 0
    odd_sum = 0
    for element in digits:
        if int(element) % 2 == 0:
            even_sum += int(element)
        elif int(element) % 2 != 0:
            odd_sum += int(element)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


given_digit = input()
result = sum_even_and_odd(given_digit)
print(result)
