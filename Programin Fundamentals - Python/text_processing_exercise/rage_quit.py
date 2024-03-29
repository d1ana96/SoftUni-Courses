text = input().upper()
unique_symbols = ''
current_symbol = ''
repetitions = ''

for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index]
    else:
        for check_next_symbol in range(index, len(text)):
            if not text[check_next_symbol].isdigit():
                break
            else:
                repetitions += text[check_next_symbol]
        repetitions = int(repetitions)
        unique_symbols += repetitions * current_symbol
        current_symbol = ''
        repetitions = ''

print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)
