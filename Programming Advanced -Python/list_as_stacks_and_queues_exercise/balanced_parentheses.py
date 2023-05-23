expression = input()

opening_brackets_stack = []
balanced = True

for character in expression:
    if character in '({[':
        opening_brackets_stack.append(character)

    elif not opening_brackets_stack:
        balanced = False
        break

    else:
        last_opening_bracket = opening_brackets_stack.pop()
        if f'{last_opening_bracket}{character}' not in '(){}[]':
            balanced = False
            break

if balanced and not opening_brackets_stack:
    print("YES")
else:
    print("NO")
