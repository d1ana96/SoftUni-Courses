numbers = input().split(", ")
numbers = list(map(int, numbers))

even_indexes_numbers = []

for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        even_indexes_numbers.append(index)
print(even_indexes_numbers)

