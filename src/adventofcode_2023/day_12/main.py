from pathlib import Path
import re

from tqdm import tqdm


def count_groups(condition) -> list[int]:
    """Find all groups of # in condition and count them."""
    return list(map(len, re.findall("#+", condition)))


def is_valid(condition, groups) -> bool:
    """Return True when the #-groups in condition match those from groups."""
    return count_groups(condition) == groups


def get_possible_conditions(condition) -> list[str]:
    """Get all combinations of replacing every ? with a . or #."""
    if "?" not in condition:
        return [condition]

    index = condition.index("?")
    conditions = []
    for char in [".", "#"]:
        new_condition = condition[:index] + char + condition[index + 1 :]
        conditions.extend(get_possible_conditions(new_condition))

    return conditions


def _get_arrangements(condition: str, groups: list[int]) -> int:
    """Get all possible arrangements and count those that are valid."""
    arrangements = 0
    for filled in get_possible_conditions(condition):
        if is_valid(filled, groups):
            arrangements += 1
    return arrangements


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    total = 0
    for line in tqdm(input_data):
        condition, groups = line.split(" ")
        groups = list(map(int, groups.split(",")))
        total += _get_arrangements(condition, groups)

    return total


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    total = 0
    for line in tqdm(input_data):
        condition, groups = line.split(" ")
        groups = list(map(int, groups.split(",")))
        condition_larger = "?".join([condition] * 5)
        groups_larger = groups * 5
        total += _get_arrangements(condition_larger, groups_larger)

    return total


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 21

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 525152

    result = part_2("input.txt")
    print(result)
