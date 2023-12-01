with open("d1.txt") as f:
    data = f.read()
data = data.split("\n")


def keep_numbers(line):
    return "".join([c for c in line if c.isdigit()])


def take_outer(line):
    return line[0] + line[-1]


m = {
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
    for word in m:
        line = line.replace(word, word + str(m[word]) + word)
    return line


data = [replace_words(line) for line in data]
print(data[:7])
data = [keep_numbers(line) for line in data]
print(data[:7])
data = [take_outer(line) for line in data]
print(data[:7])
data = [int(line) for line in data]
print(data[:7])
print(sum(data))
