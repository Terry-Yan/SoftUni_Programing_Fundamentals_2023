from math import floor
cards = input().split(" ")
shuffles_count = int(input())
first_half = []
second_half = []
middle = floor(len(cards) / 2)

for _ in range(shuffles_count):
    new_deck = []
    first_half = cards[:middle]
    second_half = cards[middle:]

    for index in range(len(first_half)):
        new_deck.append(first_half[index])
        new_deck.append(second_half[index])

    cards = new_deck

print(cards)
