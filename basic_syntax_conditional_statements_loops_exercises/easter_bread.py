budget = float(input())
flour_price = float(input())
egg_price = flour_price * 0.75
milk_price = flour_price * 1.25

loaf_price = egg_price + flour_price + (milk_price / 4)
loaf_counter = 0
colored_eggs_counter = 0

while budget - loaf_price > 0:
    budget -= loaf_price
    loaf_counter += 1
    colored_eggs_counter += 3

    if loaf_counter % 3 == 0:
        colored_eggs_counter -= loaf_counter - 2

print(f"You made {loaf_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs "
      f"and {budget:.2f}BGN left.")
