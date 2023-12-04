import re
from collections import defaultdict
from pathlib import Path


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    points = 0
    for line in input_data:
        card, numbers = line.split(": ")
        winning, own = numbers.split("|")
        winning_numbers = set(re.findall(r"\d+", winning))
        own_numbers = set(re.findall(r"\d+", own))
        matches = winning_numbers.intersection(own_numbers)
        points += int(2 ** (len(matches) - 1))

    return points


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    cards = defaultdict(lambda: 0)
    for line in input_data:
        card, numbers = line.split(": ")
        card_number = int(re.findall(r"\d+", card)[0])
        cards[card_number] += 1
        winning, own = numbers.split("|")
        winning_numbers = set(re.findall(r"\d+", winning))
        own_numbers = set(re.findall(r"\d+", own))
        matches = winning_numbers.intersection(own_numbers)
        # add the next copies for each match and amount of the current card
        for i in range(len(matches)):
            cards[card_number + i + 1] += 1 * cards[card_number]

    return sum(cards.values())


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 13

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 30

    result = part_2("input.txt")
    print(result)
