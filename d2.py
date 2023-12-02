from dataclasses import dataclass
from functools import cached_property


def read_split(filename):
    with open(filename) as f:
        data = f.read()
    data = data.split("\n")
    return data


@dataclass
class CubePull:
    color: str
    number: int

    @property
    def possible(self):
        match self.color:
            case "red":
                return self.number <= 12
            case "green":
                return self.number <= 13
            case "blue":
                return self.number <= 14

    def __lt__(self, other):
        if other is None:
            return False
        if self.color != other.color:
            raise ValueError(f"Colors must match | {self} - {other}")
        return self.number < other.number

    def __gt__(self, other):
        if other is None:
            return True
        if self.color != other.color:
            raise ValueError(f"Colors must match | {self} - {other}")
        return self.number >= other.number

    @classmethod
    def from_str(cls, string):
        number, color = string.split(" ")
        number = int(number)
        return cls(color, number)


@dataclass
class Round:
    cubes: list[CubePull]

    def _grab(self, color):
        for cube in self.cubes:
            if cube.color == color:
                return cube
        return CubePull(color, 0)

    @property
    def red(self):
        return self._grab("red")

    @property
    def green(self):
        return self._grab("green")

    @property
    def blue(self):
        return self._grab("blue")

    @property
    def possible(self):
        return all(cube.possible for cube in self.cubes)

    @classmethod
    def from_str(cls, string):
        cubes = string.split(",")
        cubes = [CubePull.from_str(cube.strip()) for cube in cubes]
        return cls(cubes)


@dataclass
class Game:
    id: int
    rounds: list[Round]

    @property
    def possible(self):
        return all(round_.possible for round_ in self.rounds)

    @cached_property
    def max(self):
        reds = sorted([round_.red for round_ in self.rounds])
        greens = sorted([round_.green for round_ in self.rounds])
        blues = sorted([round_.blue for round_ in self.rounds])
        return (reds[-1], greens[-1], blues[-1])

    @property
    def power(self):
        print(
            f"Game {self.id}: {self.max[0].number} * {self.max[1].number} * {self.max[2].number}"
        )
        return self.max[0].number * self.max[1].number * self.max[2].number

    @classmethod
    def from_str(cls, string):
        id_, rounds = string.split(":")
        id_ = int(id_.replace("Game ", ""))
        rounds = rounds.split(";")
        rounds = [Round.from_str(round_) for round_ in rounds]
        return cls(id_, rounds)


def main():
    games = read_split("d2.txt")
    games = [Game.from_str(game) for game in games]
    # Star 1
    print(sum(game.id for game in games if game.possible))
    # Star 2
    print(sum(game.power for game in games))


if __name__ == "__main__":
    main()
