text = input()
letters = ""
digits = ""
symbols = ""

for character in text:
    if character.isalpha():
        letters += character
    elif character.isdigit():
        digits += character
    else:
        symbols += character

print(digits)
print(letters)
print(symbols)
