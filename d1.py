def read_split(filename):
    with open(filename) as f:
        data = f.read()
    data = data.split("\n")
    return data


def keep_numbers(line):
    return "".join([c for c in line if c.isdigit()])


def take_outer(line):
    return line[0] + line[-1]


number_to_number = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def replace_words(line):
    for word in number_to_number:
        line = line.replace(word, word + str(number_to_number[word]) + word)
    return line


def star_1(filename):
    data = read_split(filename)
    data = [keep_numbers(line) for line in data]
    data = [take_outer(line) for line in data]
    data = [int(line) for line in data]
    return sum(data)


def star_2(filename):
    data = read_split(filename)
    # addresses extra prompt
    data = [replace_words(line) for line in data]
    data = [keep_numbers(line) for line in data]
    data = [take_outer(line) for line in data]
    data = [int(line) for line in data]
    return sum(data)


def main():
    print("Star 1:\n", star_1("d1.txt"))
    print("Star 2:\n", star_2("d1.txt"))


if __name__ == "__main__":
    main()
