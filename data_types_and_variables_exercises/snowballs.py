from sys import maxsize
from math import floor

number_of_snowballs = int(input())
max_value = -maxsize
max_snowball_weight = 0
max_time_per_snowball = 0
max_snowball_quality = 0

for _ in range(1, number_of_snowballs + 1):
    snowball_weight = int(input())
    time_per_snowball = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / time_per_snowball) ** snowball_quality

    if snowball_value > max_value:
        max_value = floor(snowball_value)
        max_snowball_weight = snowball_weight
        max_time_per_snowball = time_per_snowball
        max_snowball_quality = snowball_quality

print(f"{max_snowball_weight} : {max_time_per_snowball} = {max_value} ({max_snowball_quality})")
