from math import pi
type_of_the_figure = input()
result = 0

if type_of_the_figure == "square":
    side_a = float(input())
    result = side_a * side_a
elif type_of_the_figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    result = side_a * side_b
elif type_of_the_figure == "circle":
    radius = float(input())
    result = (radius ** 2) * pi
elif type_of_the_figure == "triangle":
    side_a = float(input())
    height = float(input())
    result = (side_a * height) / 2
print(f"{result:.3f}")
