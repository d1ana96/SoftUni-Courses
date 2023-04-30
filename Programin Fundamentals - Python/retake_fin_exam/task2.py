import re

number_inputs = int(input())
pattern = re.compile(
    r"([*|@])(?P<Tag>[A-Z][a-z]{2,})\1: "
    r"(([\[])(?P<First>[A-z])([]])\|)(([\[])(?P<Second>[A-z])([]])\|)(([\[])(?P<Third>[A-z])([]])\|)$")


for line in range(number_inputs):
    letters = []
    message = input()
    result = re.finditer(pattern, message)

    for show in result:

        tag = show["Tag"]
        letters.append(show["First"])
        first_letter = show["First"]
        letters.append(show["Second"])
        second_letter = show["Second"]
        letters.append(show["Third"])
        third_letter = show["Third"]

        if letters:
            print(f"{tag}: {ord(first_letter)} {ord(second_letter)} {ord(third_letter)}")

    if not letters:
        print("Valid message not found!")





