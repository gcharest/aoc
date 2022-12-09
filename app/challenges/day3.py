def set_compartments(line):
    half = int(len(line) / 2)
    comp1, comp2 = line[:half], line[half:]
    common = ''.join(set(comp1) & set(comp2))
    return [comp1, comp2, common]


# def order_compartments(compartments):
def priority(letter):
    pos = ord(letter)
    if pos < 97:
        pos = pos + 58
    pos = pos - 96
    return pos

def get_common(line):
    return line[2]

def sum(value):
    return value*2


def puzzle_1():
    # lines = [
    #     "vJrwpWtwJgWrhcsFMMfFFhFp",
    #     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    #     "PmmdzqPrVvPwwTWBwg",
    #     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    #     "ttgJtRGJQctTZtZT",
    #     "CrZsJsPPZsGzwwsLwLmpwMDw",
    # ]
    f = open("./challenges/day3_input1.txt", "r")
    compartments = []
    for line in f:
        compartments.append(set_compartments(line))
    
    compartment_letter = lambda compartment: compartment[2]
    compartment_letters = list(map(compartment_letter, compartments))
    priority_sum = 0
    for letter in compartment_letters:
        priority_sum += (priority(letter))
    print(priority_sum)