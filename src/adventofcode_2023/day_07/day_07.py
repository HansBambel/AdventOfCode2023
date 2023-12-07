from collections import Counter
from pathlib import Path


def _compare_value(val1, val2, part2=False) -> int:
    """Return -1 when val1 and +1 when val2 is stronger and 0 when there is a tie."""
    order = "AKQT98765432J" if part2 else "AKQJT98765432"
    if val1 == val2:
        return 0
    ind = 0
    while val1 != order[ind] and val2 != order[ind]:
        ind += 1
    return 1 if val2 == order[ind] else -1


def _compare_hands(hand1: str, hand2: str, part2=False) -> int:
    """Return -1 when left and +1 when right hand is stronger and 0 when it is a tie."""
    c_l = Counter(hand1)
    c_r = Counter(hand2)
    occ_l = c_l.most_common()
    occ_r = c_r.most_common()

    if part2:
        # convert the Js to the most common char that is not J
        js_left = c_l.get("J")
        js_right = c_r.get("J")
        if js_left and len(c_l) > 1:
            c_l.pop("J")
            c_l.update(c_l.most_common()[0][0] * js_left)
        if js_right and len(c_r) > 1:
            c_r.pop("J")
            c_r.update(c_r.most_common()[0][0] * js_right)
        occ_l = c_l.most_common()
        occ_r = c_r.most_common()

    if occ_l[0][1] == occ_r[0][1]:
        # Check if full house
        if occ_l[0][1] == 3:
            if occ_l[1][1] == 2 and occ_r[1][1] == 1:
                return -1
            elif occ_l[1][1] == 1 and occ_r[1][1] == 2:
                return 1
        # check for double pairs
        elif occ_l[0][1] == 2 and occ_r[0][1] == 2:
            if occ_l[1][1] == 2 and occ_r[1][1] == 1:
                return -1
            elif occ_l[1][1] == 1 and occ_r[1][1] == 2:
                return 1

        # check for highest card
        for i in range(len(hand1)):
            res = _compare_value(hand1[i], hand2[i], part2=part2)
            if res == 0:
                continue
            return res

    else:
        if occ_l[0][1] > occ_r[0][1]:
            return -1
        elif occ_l[0][1] < occ_r[0][1]:
            return 1
        else:
            return 0


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    hand_bids = [(line.split()[0], int(line.split()[1])) for line in input_data]

    # BUBBLESORT!
    sorted_list = [hand_bids[0]]
    for hand, bid in hand_bids[1:]:
        ind = 0
        while ind <= len(sorted_list) - 1 and _compare_hands(sorted_list[ind][0], hand) > 0:
            ind += 1
        # insert new hand here
        sorted_list.insert(ind, (hand, bid))

    total = 0
    for i, (_, bid) in enumerate(sorted_list):
        total += (i + 1) * bid
    return total


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    hand_bids = [(line.split()[0], int(line.split()[1])) for line in input_data]

    # BUBBLESORT!
    sorted_list = [hand_bids[0]]
    for hand, bid in hand_bids[1:]:
        ind = 0
        while ind <= len(sorted_list) - 1 and _compare_hands(sorted_list[ind][0], hand, part2=True) > 0:
            ind += 1
        # insert new hand here
        sorted_list.insert(ind, (hand, bid))

    total = 0
    for i, (_, bid) in enumerate(sorted_list):
        total += (i + 1) * bid
    return total


if __name__ == "__main__":
    # print("#" * 10 + " Part 1 " + "#" * 10)
    # result_ex = part_1("input_ex.txt")
    # print(result_ex)
    # assert result_ex == 6440
    #
    # result_ex = part_1("input_ex2.txt")
    # print(result_ex)
    # assert result_ex == 3542
    #
    # result_ex = part_1("input_ex3.txt")
    # print(result_ex)
    # assert result_ex == 1343
    #
    # result = part_1("input.txt")
    # assert result < 254240091
    # print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 5905

    result_ex = part_2("input_ex2.txt")
    print(result_ex)
    assert result_ex == 3667

    result_ex = part_2("input_ex3.txt")
    print(result_ex)
    assert result_ex == 1369

    result = part_2("input.txt")
    assert result > 254751210
    print(result)
