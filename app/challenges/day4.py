# each section has section_id
# each elf assigned range of id


class Assignment:
    def __init__(self, str_range):
        ranges = str_range.split("-")
        self.min = ranges[0]
        self.max = ranges[1]


def get_assignments(str):
    spread = lambda x: set(range(int(x[0]), int(x[1]) + 1))
    strs = lambda x: [x.split(",")[0].split("-"), x.split(",")[1].split("-")]
    return (spread(strs(str)[0])), (spread(strs(str)[1]))


def puzzle():
    # f = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]
    f = open("./challenges/day4_input1.txt", "r")
    is_subset = lambda x, y: x.issubset(y) or y.issubset(x)
    groups = []
    for line in f:
        groups.append(get_assignments(line))

    print(
        f"Part 1 - Number of subset pairs: {sum(list(map(lambda x: is_subset(x[0], x[1]),groups)))}"
    )
