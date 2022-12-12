class Rucksack:
    def __init__(self, content):
        self.content = content
        self.compartment_1 = content[: int(len(content) / 2)]
        self.compartment_2 = content[int(len(content) / 2) :]
        self.common_letter = "".join(set(self.compartment_1) & set(self.compartment_2))

    def get_priority(self):
        return letter_priority(self.common_letter)


class Group:
    def __init__(self, group_rucksacks):
        self.group = group_rucksacks

    def get_common_item(self):
        return "".join(
            set(self.group[0].content)
            & set(self.group[1].content)
            & set(self.group[2].content)
        ).strip()

    def get_priority(self):
        return letter_priority(self.get_common_item())


def letter_priority(letter):
    pos = ord(letter)
    if pos < 97:
        pos = pos + 58
    pos = pos - 96
    return pos


def puzzle():
    f = open("./challenges/day3_input1.txt", "r")
    rucksacks = []
    for line in f:
        rucksacks.append(Rucksack(line))

    total = sum(list(map(lambda x: x.get_priority(), rucksacks)))
    print(f"Part 1: sum  of the priorities: {total}")

    groups = [Group(rucksacks[x : x + 3]) for x in range(0, len(rucksacks), 3)]

    total = sum(list(map(lambda x: x.get_priority(), groups)))
    print(f"Part 2: sum  of the priorities: {total}")
