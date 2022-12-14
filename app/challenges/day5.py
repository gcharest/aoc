class Dock:
    def __init__(self, lines):
        self.rows = lines
        self.number_of_rows = len(lines)


class Move:
    def __init__(self, text):
        self.quantity = int(text.split(" ")[1])
        self.start = int(text.split(" ")[3])
        self.end = int(text.split(" ")[5])


def puzzle():
    f = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]

    # f = open("./challenges/day4_input1.txt", "r")

    stacks_lines = []
    move_lines = []
    for line in f:
        if line.find('move') != -1:
            move_lines.append(Move(line))
        elif line != "":
            stacks_lines.append(line)

    stacks = Dock(stacks_lines)
    print(stacks.rows)
