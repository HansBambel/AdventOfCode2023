import re
from pathlib import Path
import numpy as np


def _pred_next(diff) -> int:
    if sum(diff) == 0:
        return 0
    diff_arr = np.diff(diff)
    return diff_arr[-1] + _pred_next(diff_arr)


def _pred_before(diff) -> int:
    if sum(diff) == 0:
        return 0
    diff_arr = np.diff(diff)
    return diff_arr[0] - _pred_before(diff_arr)


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    total = 0
    for line in input_data:
        main_sequence = list(map(int, re.findall(r"-?\d+", line)))
        next_number = _pred_next(main_sequence)
        total += main_sequence[-1] + next_number

    return total


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    total = 0
    for line in input_data:
        main_sequence = list(map(int, re.findall(r"-?\d+", line)))
        next_number = _pred_before(main_sequence)
        total += main_sequence[0] - next_number

    return total


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 114

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 2

    result = part_2("input.txt")
    print(result)
