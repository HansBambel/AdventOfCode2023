import re
from pathlib import Path

from tqdm import tqdm


def _get_location(seed, mappings):
    for mapping in mappings:
        for destination, source, range_ind in mapping:
            # check if the seed is in there
            if source <= seed < source + range_ind:
                # get new location
                seed = destination + seed - source
                break
    return seed


def _get_seed_locations(seeds, mappings) -> list:
    for i, seed in enumerate(seeds):
        seeds[i] = _get_location(seed, mappings)
    return seeds


def _get_seed_paths2(seed_ranges, mappings) -> list:
    ranges = seed_ranges
    new_ranges = []
    for mapping in tqdm(mappings):
        while len(ranges) > 0:
            seed_start, seed_end = ranges.pop()
            found = False
            for destination, source, range_ind in mapping:
                map_end = source + range_ind
                offset = destination - source
                # no overlap
                if map_end < seed_start or source > seed_end:
                    continue
                # we have overlap
                if source <= seed_start and map_end >= seed_end:
                    # all seeds are in mapping
                    new_ranges.append((seed_start + offset, seed_end + offset))
                elif source <= seed_start and map_end <= seed_end:
                    # partial overlap left
                    overlap = map_end - seed_start
                    if overlap == 0:
                        continue
                    new_ranges.append((seed_start + offset, map_end + offset))
                    ranges.append((map_end, seed_end))
                elif source >= seed_start and source + range_ind <= seed_end:
                    # inner overlap
                    new_ranges.append((source + offset, map_end + offset))
                    ranges.append((seed_start, source))
                    ranges.append((map_end, seed_end))
                elif source <= seed_end and map_end >= seed_end:
                    # partial overlap right
                    overlap = seed_end - source
                    if overlap == 0:
                        continue
                    new_ranges.append((source + offset, seed_end + offset))
                    ranges.append((seed_start, source))
                else:
                    raise ValueError("Missed a case")
                found = True
            if not found:
                new_ranges.append((seed_start, seed_end))
        ranges = new_ranges
        new_ranges = []

    return ranges


def _parse_mapping(input_data) -> list[[list[tuple[int, int, int]]]]:
    parsed_mappings = []
    for mapping in input_data[1:]:
        mapping = mapping.split("\n")
        lines = [tuple(int(x) for x in re.findall(r"\d+", line)) for line in mapping[1:]]
        parsed_mappings.append(lines)
    return parsed_mappings


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n\n")
    parsed_mappings = _parse_mapping(input_data)

    seeds = list(map(int, re.findall(r"\d+", input_data[0])))
    locations = _get_seed_paths2([(seed, seed + 1) for seed in seeds], parsed_mappings)

    # get the smallest location
    min_val = 1e100
    for loc in locations:
        if loc[0] < min_val:
            min_val = loc[0]
    return min_val


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n\n")
    parsed_mappings = _parse_mapping(input_data)

    seed_ranges = list(map(int, re.findall(r"\d+", input_data[0])))
    seed_ranges = [(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]) for i in range(0, len(seed_ranges), 2)]

    locations = _get_seed_paths2(seed_ranges, parsed_mappings)
    # get the smallest location
    min_val = 1e100
    for loc in locations:
        if loc[0] < min_val:
            min_val = loc[0]
    return min_val


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
    assert result > 62988482
    assert result > 62988483
    assert result > 79032545
    assert result == 79874951
    print(result)
