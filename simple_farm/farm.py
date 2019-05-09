class Animal(object):

    def __init__(self, name: str):
        self.name = name


class Cow(Animal):

    def __init__(self, name: str, tag: int, production_rate: int):
        super().__init__(name)
        self.tag: int = tag
        self.production_rate: int = production_rate

    def milk(self) -> int:
        return self.production_rate


class Bull(Animal):

    def __init__(self, name: str):
        super().__init__(name)
