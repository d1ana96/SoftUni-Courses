destination = input()
saved_money = 0
enough_money = False

while destination != "End":
    needed_money = float(input())
    saved_money = 0
    while saved_money < needed_money:
        current_money = float(input())
        saved_money += current_money
        if saved_money >= needed_money:
            enough_money = True
            print(f"Going to {destination}!")
    destination = input()
