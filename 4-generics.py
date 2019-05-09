from overengineered_farm.farm import Fox, Milkable, Animal, Cow


def milk_animal(animal: Milkable) -> int:
    return animal.milk()


def speak_animal(animal: Animal) -> str:
    return animal.say()


fox = Fox('Ylvis', 0)
print(speak_animal(fox))
print(milk_animal(fox))

cow = Cow('Bertha', 37, 42)
print(speak_animal(cow))
print(milk_animal(cow))
