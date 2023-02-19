from math import floor

biscuits_per_worker = int(input())
number_of_workers = int(input())
competing_factory_biscuits = int(input())
total_biscuits = 0

for day in range(1, 31):
    total_biscuits_per_day = biscuits_per_worker * number_of_workers

    if day % 3 == 0:
        total_biscuits_per_day = floor(total_biscuits_per_day * 0.75)

    total_biscuits += total_biscuits_per_day

print(f"You have produced {total_biscuits} biscuits for the past month.")
difference = (competing_factory_biscuits - total_biscuits)
percentage = abs(difference) / competing_factory_biscuits * 100

if total_biscuits >= competing_factory_biscuits:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")
