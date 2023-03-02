lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_is_broken = False
sword_is_broken = False
shield_is_broken = False
armor_is_broken = False

quantity_of_broken_helmets = 0
quantity_of_broken_swords = 0
quantity_of_broken_shields = 0
quantity_of_broken_armors = 0

for current_lost_fight in range(1, lost_fights_count + 1):
    if current_lost_fight % 2 == 0:
        helmet_is_broken = True
        quantity_of_broken_helmets += 1
    if current_lost_fight % 3 == 0:
        sword_is_broken = True
        quantity_of_broken_swords += 1
        if current_lost_fight % 2 == 0:
            helmet_is_broken = True
            shield_is_broken = True
            quantity_of_broken_shields += 1
            if quantity_of_broken_shields % 2 == 0:
                armor_is_broken = True
                quantity_of_broken_armors += 1

total_costs_for_helmets = quantity_of_broken_helmets * helmet_price
total_costs_for_swords = quantity_of_broken_swords * sword_price
total_costs_for_shields = quantity_of_broken_shields * shield_price
total_costs_for_armors = quantity_of_broken_armors * armor_price

total_expenses = total_costs_for_helmets + total_costs_for_swords + total_costs_for_shields + total_costs_for_armors
print(f"Gladiator expenses: {total_expenses:.2f} aureus")
