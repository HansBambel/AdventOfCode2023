import math
import re
from pathlib import Path

from tqdm import tqdm


def _get_winnings(time, distance) -> int:
    wins = 0
    for i in tqdm(range(time + 1)):
        if (time - i) * i > distance:
            wins += 1
    return wins


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    time_distance = list(zip(*[map(int, re.findall(r"\d+", line)) for line in input_data]))
    # get winning combinations
    winning_combinations = [_get_winnings(time, distance) for time, distance in time_distance]
    return math.prod(winning_combinations)


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    time_distance = list(zip(*[map(int, re.findall(r"\d+", line.replace(" ", ""))) for line in input_data]))
    # get winning combinations
    winning_combinations = [_get_winnings(time, distance) for time, distance in time_distance]
    return math.prod(winning_combinations)


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 288

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 71503

    result = part_2("input.txt")
    print(result)
