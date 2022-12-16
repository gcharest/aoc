import re


class Move:
    """Takes a string, returns the quantity of blocks to move,
    which stack the moves start and which stack it ends."""

    def __init__(self, text):
        self.quantity = int(text.split(" ")[1])
        self.start = int(text.split(" ")[3])
        self.end = int(text.split(" ")[5])


class Dock:
    def __init__(self, lines):
        get_integers = lambda x: re.findall(r"\d+", x)
        self.lines = lines
        self.data_rows = lines[:-1]
        self.indexes_row = lines[len(lines) - 1]
        self.stacks_indexes = get_integers(self.indexes_row)

    def get_stacks(self):
        cols = []
        for index, char in enumerate(self.indexes_row):
            cols.append([char])
        for row in reversed(self.data_rows):
            for index, char in enumerate(row):
                if char != " ":
                    cols[index].append(char)
        cols = [sub for sub in cols if sub[0] in self.stacks_indexes]
        for col in cols:
            col = [sub for sub in col if sub != " "]
        return cols


def move_crate_9000(stacks, move):
    moves = move.quantity
    if moves >= len(stacks[move.start - 1]):
        moves = len(stacks[move.start - 1]) - 1
    for i in range(moves):
        crate = stacks[move.start - 1].pop()
        stacks[move.end - 1].append(crate)

    return stacks


def move_crate_9001(stacks, move):
    moves = move.quantity
    if moves >= len(stacks[move.start - 1]):
        moves = len(stacks[move.start - 1]) - 1
    index = len(stacks[move.start - 1]) - moves
    for i in range(moves):
        crate = stacks[move.start - 1].pop(index)
        stacks[move.end - 1].append(crate)

    return stacks


def print_stacks(stacks):
    for stack in stacks:
        print(stack)


def get_top_crates(stacks):
    top_crates = []
    for stack in stacks:
        top_crates.append(stack[len(stack) - 1])
    return "".join(top_crates)


def puzzle():
    """Prints the results of the puzzle"""

    # Example input
    # f = [
    #     "    [D]    ",
    #     "[N] [C]    ",
    #     "[Z] [M] [P]",
    #     " 1   2   3 ",
    #     "",
    #     "move 1 from 2 to 1",
    #     "move 3 from 1 to 3",
    #     "move 2 from 2 to 1",
    #     "move 1 from 1 to 2",
    # ]

    f = open("./challenges/day5_input1.txt", "r", newline=None)

    stacks_lines = []
    move_lines = []
    for line in f:
        if line.find("move") != -1:
            move_lines.append(Move(line))
        elif len(line) > 2:
            stacks_lines.append(line)

    docks = Dock(stacks_lines)

    stacks_9000 = docks.get_stacks()
    stacks_9001 = docks.get_stacks()

    for move in move_lines:
        stacks_9000 = move_crate_9000(stacks_9000, move)
        stacks_9001 = move_crate_9001(stacks_9001, move)
    print(f"Part 1: {get_top_crates(stacks_9000)}")
    print(f"Part 2: {get_top_crates(stacks_9001)}")
