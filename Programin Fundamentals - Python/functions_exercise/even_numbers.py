numbers = [int(x) for x in input().split()]
result_even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(result_even_numbers)
