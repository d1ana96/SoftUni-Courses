words = input().split()
palindrome = input()
palindrome_list = []

for word in words:
    reversed_list_of_letters = reversed(word)
    reversed_word = "".join(reversed_list_of_letters)

    if reversed_word == word:
        palindrome_list.append(word)
print(palindrome_list)
palindrome_count = words.count(palindrome)
print(f"Found palindrome {palindrome_count} times")
