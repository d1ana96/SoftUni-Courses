def is_valid_length(password):
    return 6 <= len(password) <= 10


def contains_alpha_numeric_chars(password):
    return password.isalnum()


def contains_two_digit(password):
    count_digits = 0
    for element in password:
        if element.isdigit():
            count_digits += 1
    return count_digits >= 2


input_password = input()
is_valid = True

if not is_valid_length(input_password):
    is_valid = False
    print(f"Password must be between 6 and 10 characters")
if not contains_alpha_numeric_chars(input_password):
    is_valid = False
    print("Password must consist only of lettres and digits")
if not contains_two_digit(input_password):
    is_valid = False
    print(f"Password must have at least 2 digits")
if is_valid:
    print("Password is valid")

