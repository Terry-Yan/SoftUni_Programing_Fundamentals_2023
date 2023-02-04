lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_break_counter = 0
sword_break_counter = 0
shield_break_counter = 0
armor_break_counter = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0 and fight % 3 == 0:
        helmet_break_counter += 1
        sword_break_counter += 1
        shield_break_counter += 1

        if shield_break_counter % 2 == 0:
            armor_break_counter += 1
    elif fight % 2 == 0:
        helmet_break_counter += 1
    elif fight % 3 == 0:
        sword_break_counter += 1

expenses = (helmet_break_counter * helmet_price) + (sword_break_counter * sword_price) + \
           (shield_break_counter * shield_price) + (armor_break_counter * armor_price)
print(f"Gladiator expenses: {expenses:.2f} aureus")
