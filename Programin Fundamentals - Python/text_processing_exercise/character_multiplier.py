words = input().split()

first_word = words[0]
second_word = words[1]

min_len = min(len(first_word), len(second_word))
result = 0

for index in range(min_len):
    first_word_char = first_word[index]
    second_word_char = second_word[index]
    result += ord(first_word_char) * ord(second_word_char)

for index in range(min_len, len(first_word)):
    result += ord(first_word[index])

for index in range(min_len, len(second_word)):
    result += ord(second_word[index])

print(result)


