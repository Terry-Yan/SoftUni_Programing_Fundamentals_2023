fire_info = input().split("#")
water = int(input())
putted_out_fires = []

for index in range(len(fire_info)):
    current_fire = fire_info[index].split(" = ")
    fire_type = current_fire[0]
    fire_value = int(current_fire[1])

    if fire_type == "High" and (fire_value < 81 or fire_value > 125):
        continue

    if fire_type == "Medium" and (fire_value < 51 or fire_value > 80):
        continue

    if fire_type == "Low" and (fire_value < 1 or fire_value > 50):
        continue

    if fire_value > water:
        continue

    water -= fire_value
    putted_out_fires.append(fire_value)

print("Cells:")
for index in range(len(putted_out_fires)):
    print(f" - {putted_out_fires[index]}")
total_fire = sum(putted_out_fires)
effort = 0.25 * total_fire
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
