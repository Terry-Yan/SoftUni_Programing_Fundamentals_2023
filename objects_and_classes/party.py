class Party:
    def __init__(self):
        self.people = []


party = Party()
line = input()

while line != "End":
    party.people.append(line)
    line = input()

people = ", ".join(party.people)
total_going_people = len(party.people)
print(f"Going: {people}")
print(f"Total: {total_going_people}")
