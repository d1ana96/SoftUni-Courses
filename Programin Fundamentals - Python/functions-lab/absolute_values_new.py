numbers = [float(x) for x in input().split()]
abs_numbers = []

for number in numbers:
    abs_numbers.append(abs(number))
print(abs_numbers)


# numbers = [abs(float(x)) for x in input().split()]
# print(numbers)
