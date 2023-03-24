def perfect_number(some_number):
    sum_numbers = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            sum_numbers += divisor
    return sum_numbers == some_number


given_number = int(input())

if perfect_number(given_number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
