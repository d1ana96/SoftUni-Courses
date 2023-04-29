deliverers = {}
clients = {}
total_spent_money_from_all_clients = 0

while True:

    command = input().split()
    if command[0] == "End":
        break

    if command[0] == "Deliver":
        distributor_name = command[1]
        spent_money_to_that_distributor = float(command[2])

        if distributor_name not in deliverers:
            deliverers[distributor_name] = {"current_money": spent_money_to_that_distributor,
                                            "total_spent_money": spent_money_to_that_distributor}
        else:
            deliverers[distributor_name]["current_money"] += spent_money_to_that_distributor
            deliverers[distributor_name]["total_spent_money"] += spent_money_to_that_distributor

    elif command[0] == "Return":
        distributor_name = command[1]
        returned_money = float(command[2])

        if distributor_name not in deliverers:
            continue
        else:
            if returned_money > deliverers[distributor_name]["total_spent_money"]:
                continue
            deliverers[distributor_name]["current_money"] -= returned_money

        if deliverers[distributor_name]["current_money"] <= 0:
            del deliverers[distributor_name]


    elif command[0] == "Sell":
        client_name = command[1]
        money_earned_from_that_client = float(command[2])
        total_spent_money_from_all_clients += money_earned_from_that_client

        if client_name not in clients:
            clients[client_name] = money_earned_from_that_client
        else:
            clients[client_name] += money_earned_from_that_client



for client, money in clients.items():
    print(f"{client}: {money:.2f}")
print("-----------")

for deliverer, values in deliverers.items():
    print(f"{deliverer}: {deliverers[deliverer]['total_spent_money']:.2f}")

print("-----------")
print(f"Total Income: {total_spent_money_from_all_clients:.2f}")
