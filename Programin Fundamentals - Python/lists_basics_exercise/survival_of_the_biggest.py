list_numbers_as_string = input().split()
list_integers = list(map(int, list_numbers_as_string))
count = int(input())

for number in range(count):
    min_number = min(list_integers)
    list_numbers_as_string.remove(str(min_number))
    list_integers.remove(min_number)

print(", ".join(list_numbers_as_string))
