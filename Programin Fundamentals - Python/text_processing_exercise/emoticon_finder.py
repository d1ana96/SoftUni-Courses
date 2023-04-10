text = input()
for index in range(len(text)):
    char = text[index]
    if char == ":" and index + 1 < len(text):
        symbol = text[index+1]
        print(f':{symbol}')
        