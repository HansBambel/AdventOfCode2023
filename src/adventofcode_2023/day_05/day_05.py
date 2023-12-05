import re
from pathlib import Path
from joblib import Parallel, delayed
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
    results = []
    for seed_range in seed_ranges:
        new_results = Parallel(n_jobs=16)(delayed(_get_location)(seed, mappings) for seed in tqdm(seed_range))
        results.extend(new_results)
    # for i, seed in enumerate(seeds):
    #     seeds[i] = _get_location(seed, mappings)
    return results


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
    locations = _get_seed_locations(seeds, parsed_mappings)
    # get the smallest location
    return min(locations)


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n\n")
    parsed_mappings = _parse_mapping(input_data)

    seed_ranges = list(map(int, re.findall(r"\d+", input_data[0])))
    seed_ranges = [range(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]) for i in range(0, len(seed_ranges), 2)]

    locations = _get_seed_paths2(seed_ranges, parsed_mappings)
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
