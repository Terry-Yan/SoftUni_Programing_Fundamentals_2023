quantity_of_decorations = int(input())
days_left_until_christmas = int(input())
current_day = 0
budget = 0
points = 0

for _ in range(days_left_until_christmas, 0, -1):
    current_day += 1

    if current_day % 11 == 0:
        quantity_of_decorations += 2

    if current_day % 2 == 0:
        budget += quantity_of_decorations * 2
        points += 5

    if current_day % 3 == 0:
        budget += (quantity_of_decorations * 5) + (quantity_of_decorations * 3)
        points += 3 + 10

    if current_day % 5 == 0:
        budget += quantity_of_decorations * 15
        points += 17
        if current_day % 3 == 0:
            points += 30

    if current_day % 10 == 0:
        points -= 20
        budget += 5 + 3 + 15

if current_day % 10 == 0:
    points -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {points}")
