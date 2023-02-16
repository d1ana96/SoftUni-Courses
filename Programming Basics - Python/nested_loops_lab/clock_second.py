hours = 0
minutes = 0

while hours < 24:
    while minutes < 60:
        print(f"{hours}:{minutes}")
        minutes += 1
    minutes = 0
    hours += 1
