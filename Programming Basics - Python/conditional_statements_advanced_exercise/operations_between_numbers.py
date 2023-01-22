first_number = int(input())
second_number = int(input())
operator = input()
result = 0
type_result = ""

if operator == "+":
    result = first_number + second_number
    if result % 2 == 0:
        type_result = "even"
    else:
        type_result = "odd"
    print(f"{first_number} + {second_number} = {result} - {type_result}")

elif operator == "-":
    result = first_number - second_number
    if result % 2 == 0:
        type_result = "even"
    else:
        type_result = "odd"
    print(f"{first_number} - {second_number} = {result} - {type_result}")

elif operator == "*":
    result = first_number * second_number
    if result % 2 == 0:
        type_result = "even"
    else:
        type_result = "odd"
    print(f"{first_number} * {second_number} = {result} - {type_result}")

elif operator == "/":
    if second_number == 0:
        print(f" Cannot divide {first_number} by zero")
    else:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result:.2f}")

elif operator == "%":
    if second_number == 0:
        print(f" Cannot divide {first_number} by zero")
    else:
        result = first_number % second_number
        print(f"{first_number} % {second_number} = {result}")

