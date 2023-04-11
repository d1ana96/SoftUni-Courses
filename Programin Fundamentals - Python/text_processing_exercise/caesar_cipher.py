text = input()
encrypted_text = ""

for character in text:
    new_ascii_value = ord(character) + 3
    encrypted_text += chr(new_ascii_value)

print(encrypted_text)
