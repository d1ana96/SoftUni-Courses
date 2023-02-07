needed_trip_money = float(input())
available_money = float(input())
total_days = 0
spending_days = 0

while spending_days < 5:
    command = input()
    current_money = float(input())
    total_days += 1

    if command == "spend":
        spending_days += 1
        if current_money > available_money:
            available_money = 0
        else:
            available_money -= current_money
            
        if spending_days == 5:
            print(f"You can't save the money.")
            print(f"{total_days}")
            break

    elif command == "save":
        available_money += current_money
        spending_days = 0
        if available_money >= needed_trip_money:
            print(f"You saved the money for {total_days} days.")
            break


