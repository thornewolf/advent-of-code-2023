from dataclasses import dataclass
from functools import *
from itertools import *


def read_split(filename):
    with open(filename) as f:
        data = f.read()
    data = data.split("\n")
    return data


def main():
    ...


if __name__ == "__main__":
    main()
