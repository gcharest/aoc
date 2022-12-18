def is_unique_string(sub, sub_len):
    is_unique = True
    for i in range(sub_len):
        if sub.count(sub[i]) > 1:
            is_unique = False
    return is_unique


def find_marker(packet, sub_len):
    position = sub_len
    for i in range(len(packet) - sub_len):
        marker = packet[position - sub_len : position]
        if is_unique_string(marker, sub_len) == True:
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
    messages = []
    for packet in f:
        packets.append(find_marker(packet, 4))
        messages.append(find_marker(packet, 14))

    print(f"Part 1: {packets[0]}")
    print(f"Part 2: {messages[0]}")
    
