current_version = [int(x) for x in input().split(".")]
carry_over = 1

for index in range(len(current_version) - 1, - 1, -1):
    current_version[index] += carry_over

    if current_version[index] == 10:
        current_version[index] = 0
        carry_over = 1
    else:
        carry_over = 0

print(f"{current_version[0]}.{current_version[1]}.{current_version[2]}")
