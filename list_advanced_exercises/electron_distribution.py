elections = int(input())
shells = []

while elections > 0:
    for index in range(1, elections + 1):
        current_shell_capacity = 2 * (index ** 2)

        if elections - current_shell_capacity <= 0:
            shells.append(elections)
            elections = 0
            break
        else:
            shells.append(current_shell_capacity)
            elections -= current_shell_capacity

print(shells)
