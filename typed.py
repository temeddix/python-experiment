from typing import Protocol, Self


class Clone(Protocol):
    def clone(self) -> Self:
        """Return a clone of the object."""
        ...


class Transform(Protocol):
    def move(self, x: float, y: float) -> Self:
        """Move the object to a new position."""
        ...


class Position:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def clone(self):
        return Position(
            x=self.x,
            y=self.y,
        )

    def move(self, x: float, y: float):
        return Position(
            x=self.x + x,
            y=self.y + y,
        )


def clone_things(position: Position) -> list[Clone]:
    return [
        position.clone(),
        position.clone(),
    ]


def transform_things(position: Position) -> list[Transform]:
    return [
        position.move(3, 4),
        position.move(5, 6),
    ]
