from challenges import day1, day2, day3, day4


def day(num):
    return f"\n\n---\nAOC Day {num}\n---\n"


def main():
    print(day(1))
    day1.puzzle_1()
    print(day(2))
    day2.puzzle_1()
    print(day(3))
    day3.puzzle()
    print(day(4))
    day4.puzzle()


main()
