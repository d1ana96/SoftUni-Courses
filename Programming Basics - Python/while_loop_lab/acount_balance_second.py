command = input()
total_money = 0

while command != "NoMoreMoney":
    if float(command) < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {float(command):.2f}")
    total_money += float(command)
    command = input()
print(f"Total: {total_money:.2f}")
