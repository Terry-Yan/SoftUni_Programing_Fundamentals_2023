#Needs rework!!!!

list_of_items = input().split("|")
budget = float(input())
sold_items = []
total_profit = 0
total_money = 0

for index in range(len(list_of_items)):
    current_item = list_of_items[index].split("->")
    item_type = current_item[0]
    item_price = float(current_item[1])

    if item_type == "Clothes" and item_price > 50.00:
        continue

    if item_type == "Shoes" and item_price > 35.00:
        continue

    if item_type == "Accessories" and item_price > 20.50:
        continue

    if budget < item_price:
        continue

    budget -= item_price
    sell_price = round(1.40 * item_price, 2)
    total_money += sell_price
    profit = sell_price - item_price
    total_profit += profit
    sold_items.append(sell_price)

print(*sold_items)
print(f"Profit: {total_profit:.2f}")
if total_money + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
