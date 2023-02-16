start = int(input())
end = int(input())
magic_number = int(input())
combinations_count = 0
is_found = False
first_number = 0
second_number = 0

for first_number in range(start, end + 1):
    for second_number in range(start, end + 1):
        combinations_count += 1
        if first_number + second_number == magic_number:
            is_found = True
            break
    if is_found:
        break
if is_found:
    print(f"Combination N:{combinations_count} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combinations_count} combinations - neither equals {magic_number}")
