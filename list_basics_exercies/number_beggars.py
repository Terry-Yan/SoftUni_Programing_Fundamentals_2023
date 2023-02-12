numbers = input().split(", ")
beggars_count = int(input())
money = [0] * beggars_count

for index in range(len(numbers)):
    active_beggar = index % beggars_count
    bounty = int(numbers[index])
    money[active_beggar] += bounty

print(money)
