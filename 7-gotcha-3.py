from __future__ import annotations


class Position:
    def __init__(self, pos: int):
        self.pos = pos

    def __add__(self, other: Position) -> Position:
        return Position(self.pos + other.pos)
