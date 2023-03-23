def palindrome_integer(numbers_list):
    for number in numbers_list:
        reversed_number = number[::-1]
        if reversed_number == number:
            print(True)
        else:
            print(False)


given_numbers = input().split(', ')
result = palindrome_integer(given_numbers)
