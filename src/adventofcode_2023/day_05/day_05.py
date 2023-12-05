import re
from pathlib import Path


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n\n")
    seeds = re.findall(r"\d+", input_data[0])
    seeds_path = [[int(seed)] for seed in seeds]
    input_data = input_data[1:]
    for seed_path in seeds_path:
        for mapping in input_data:
            mapping = mapping.split("\n")
            locations = mapping[1:]
            # Add the identity and change it later
            seed_path.append(seed_path[-1])
            found = False
            for location in locations:
                if found:
                    break
                # destination, source, range
                destination, source, range_ind = (int(x) for x in re.findall(r"\d+", location))
                # check if the seed is in there
                if seed_path[-1] in range(source, source + range_ind):
                    found = True
                    seed_path[-1] = destination + seed_path[-1] - source

    # get the smallest location
    locations = [path[-1] for path in seeds_path]
    return min(locations)


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


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
