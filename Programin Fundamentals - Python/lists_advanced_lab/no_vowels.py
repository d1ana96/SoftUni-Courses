vowels = ["a", "o", "u", "e", "i"]
text = input()

no_vowel_text = [character for character in text if character not in vowels]
print("".join(no_vowel_text))
