# broken on purpose because of forward use or use within type definition


class PositionBroken:
    def __init__(self, pos: int):
        self.pos = pos

    def __add__(self, other: PositionBroken) -> PositionBroken:
        return PositionBroken(self.pos + other.pos)