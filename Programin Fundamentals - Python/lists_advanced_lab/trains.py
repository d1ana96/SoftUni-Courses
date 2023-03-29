number_wagons = int(input())

train = [0 for index in range(number_wagons)]

command = input()

while command != "End":
    explode = command.split()

    current_command = explode[0]

    if current_command == "add":
        number_people = int(explode[1])
        train[-1] += number_people
    if current_command == "insert":
        position = int(explode[1])
        number_people = int(explode[2])
        train[position] += number_people
    if current_command == "leave":
        position = int(explode[1])
        number_people = int(explode[2])
        train[position] -= number_people

    command = input()
    
print(train)
