def puzzle_1():
    f = open("./challenges/calories.txt", "r")
    elves = []
    buffer = []
    for line in f:
        if len(line) != 1:
            buffer.append(int(line))
        else:
            elves.append(sum(buffer))
            buffer = []

    i = 0
    total = 0
    while i < 3:
        max_val = max(elves)
        index_max = elves.index(max_val)
        total += elves.pop(index_max)
        print(
            f"\nelves count: {len(elves)}\nmax_val: {max_val}\nindex_max: {index_max}\ntotal: {total}"
        )
        i += 1

