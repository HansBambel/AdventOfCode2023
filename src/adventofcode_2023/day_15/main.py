import re
from collections import OrderedDict, defaultdict
from pathlib import Path


def get_hash_value(chars: str):
    hash_value = 0
    for char in chars:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256
    return hash_value


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    sequence = data_file.split(",")
    value = 0
    for chars in sequence:
        hash_value = get_hash_value(chars)
        value += hash_value
    return value


def calc_focusing_power(my_map):
    focusing_power = 0
    for key, lenses in my_map.items():
        for i, focal_power in enumerate(lenses.values()):
            focusing_power += (key + 1) * (i + 1) * focal_power
    return focusing_power


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    sequence = data_file.split(",")
    my_map: defaultdict[int, OrderedDict[str, int]] = defaultdict(lambda: OrderedDict())

    for chars in sequence:
        label = re.findall(r"\w+", chars)[0]
        hash_value = get_hash_value(label)
        if "-" in chars:
            if label in my_map[hash_value]:
                my_map[hash_value].pop(label)
        else:
            value = int(re.findall(r"\d+", chars)[0])
            my_map[hash_value][label] = value

    focusing_power = calc_focusing_power(my_map)
    return focusing_power


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 1320

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 145

    result = part_2("input.txt")
    print(result)
