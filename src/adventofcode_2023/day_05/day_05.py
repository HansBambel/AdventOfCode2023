import re
from pathlib import Path


def _get_location(seed, mappings):
    for mapping in mappings:
        mapping = mapping.split("\n")
        lines = mapping[1:]
        for line in lines:
            # destination, source, range
            destination, source, range_ind = (int(x) for x in re.findall(r"\d+", line))
            # check if the seed is in there
            if seed in range(source, source + range_ind):
                seed = destination + seed - source
                break
    return seed


def _get_seed_paths(seeds, mappings) -> list:
    for i, seed in enumerate(seeds):
        seeds[i] = _get_location(seed, mappings)
    return seeds


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n\n")
    seeds = list(map(int, re.findall(r"\d+", input_data[0])))

    locations = _get_seed_paths(seeds, input_data[1:])
    # get the smallest location
    return min(locations)


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n\n")
    seed_ranges = re.findall(r"\d+", input_data[0])
    seeds = []
    for i in range(0, len(seed_ranges), 2):
        start, range_ind = int(seed_ranges[i]), int(seed_ranges[i + 1])
        seeds += list(range(start, start + range_ind))
    seeds = list(map(int, seeds))
    locations = _get_seed_paths(seeds, input_data[1:])
    # get the smallest location
    return min(locations)


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 35

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 46

    result = part_2("input.txt")
    print(result)
