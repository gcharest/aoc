from challenges import day1, day2, day3, day4, day5, day6


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
    print(day(5))
    day5.puzzle()
    print(day(6))
    day6.puzzle()


main()
