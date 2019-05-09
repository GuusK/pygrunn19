from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, tag: int):
        self.name = name
        self.tag = tag

    @abstractmethod
    def say(self) -> str:
        pass


class Milkable(Animal, ABC):
    def __init__(self, name: str, tag: int, production_rate: int):
        super().__init__(name, tag)
        self.production_rate = production_rate

    def milk(self):
        return self.production_rate


class Fox(Animal):

    def say(self) -> str:
        return 'Ring-ding-ding-ding-dingeringeding!'


class Goat(Milkable):

    def say(self) -> str:
        return 'Maaa'


class Bull(Animal):

    def say(self) -> str:
        return 'MOO!'


class Cow(Milkable):
    def say(self) -> str:
        return 'moo'
