class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        line = ""
        if species == "mammal":
            line += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            line += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            line += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        line += f"Total animals: {Zoo.__animals}"
        return line


zoo_name = input()
number = int(input())

my_zoo = Zoo(zoo_name)

for _ in range(number):
    entry_info = input().split()
    animal_type = entry_info[0]
    animal_name = entry_info[1]

    my_zoo.add_animal(animal_type, animal_name)

animal_type_query = input()
print(my_zoo.get_info(animal_type_query))
