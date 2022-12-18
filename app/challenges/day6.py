def is_unique_string(sub):
    is_unique = True
    for i in range(4):
        if sub.count(sub[i]) > 1:
            is_unique = False
    return is_unique


def find_marker(packet):
    position = 4
    for i in range(len(packet) - 4):
        marker = packet[position - 4 : position]
        if is_unique_string(marker) == True:
            return(position, marker)
        position += 1
    return (position, marker)



def puzzle():
    f = open("./challenges/day6_input1.txt", "r", newline=None)
    # f = [
    #     "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    #     "bvwbjplbgvbhsrlpgdmjqwftvncz",
    #     "nppdvjthqldpwncqszvftbrmjlhg",
    #     "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    #     "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
    # ]

    packets =[] 
    for packet in f:
        packets.append(find_marker(packet))
    print(f"Part 1: {packets[0]}")