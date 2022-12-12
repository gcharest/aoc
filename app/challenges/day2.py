HAND_VALUES = dict(rock=1, paper=2, scissors=3)
HAND_WINNER = dict(rock="scissors", paper="rock", scissors="paper")


def calculate_round_score(opponent, play):
    if opponent == play:
        return 3 + HAND_VALUES[play]
    if HAND_WINNER[opponent] == play:
        return 0 + HAND_VALUES[play]
    else:
        return 6 + HAND_VALUES[play]


def find_play(opponent, outcome):
    if outcome == "draw":
        return opponent
    elif outcome == "win":
        return next(
            hand
            for hand in HAND_WINNER
            if calculate_round_score(opponent, hand) == 6 + HAND_VALUES[hand]
        )
    elif outcome == "lose":
        return next(
            hand
            for hand in HAND_WINNER
            if calculate_round_score(opponent, hand) == 0 + HAND_VALUES[hand]
        )


def calculate_total_score(rounds, mapping, type=""):
    total = 0
    for r in rounds:
        opponent = mapping[r["opponent"]]
        if type == "play":
            play = mapping[r["play"]]
        else:
            play = find_play(opponent, mapping[r["play"]])

        r_score = calculate_round_score(opponent, play)
        total += r_score
    return total


def puzzle_1():
    rounds = []

    f = open("./challenges/day2_input1.txt", "r")
    for line in f:
        rounds.append(dict(opponent=line[0], play=line[2]))

    input_mapping = dict(
        A="rock", B="paper", C="scissors", X="rock", Y="paper", Z="scissors"
    )
    outcome_mapping = dict(
        A="rock", B="paper", C="scissors", X="lose", Y="draw", Z="win"
    )

    total = calculate_total_score(rounds, input_mapping, "play")
    total_2 = calculate_total_score(rounds, outcome_mapping)

    print(f"Part 1 final score: {total}\nPuzzle 2 final score: {total_2}")
