import re

text = input().lower()
searched_target = input().lower()

pattern = fr"\b{searched_target}\b"

matches = re.findall(pattern, text)
print(len(matches))
