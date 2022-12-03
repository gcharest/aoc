from challenges import day1, day2


def day(num):
    return f"\n\n---\nAOC Day {num}\n---"


def main():
    print(day(1))
    day1.puzzle_1()
    print(day(2))
    day2.puzzle_1()


main()
