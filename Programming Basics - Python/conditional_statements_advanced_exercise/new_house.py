type_flower = input()
number_flower = int(input())
budget = int(input())

sum = 0

if type_flower == "Roses":
    sum = 5 * number_flower
    if number_flower > 80:
        sum = sum * 0.9
elif type_flower == "Dahlias":
    sum = 3.80 * number_flower
    if number_flower > 90:
        sum = sum * 0.85
elif type_flower == "Tulips":
    sum = 2.80 * number_flower
    if number_flower > 80:
        sum = sum * 0.85
elif type_flower == "Narcissus":
    sum = 3 * number_flower
    if number_flower < 120:
        sum = sum + (sum * 0.15)
elif type_flower == "Gladiolus":
    sum = 2.50 * number_flower
    if number_flower < 80:
        sum = sum + (sum * 0.2)

difference = abs(budget - sum)

if budget >= sum:
    print(f"Hey, you have a great garden with {number_flower} {type_flower} and {difference:.2f} leva left.")
elif budget < sum:
    print(f"Not enough money, you need {difference:.2f} leva more.")