from pathlib import Path
from itertools import combinations


def _expand_empty_space(grid):
    expanded = []
    rows_empty_add = []
    # expand rows
    for i, line in enumerate(grid):
        if "#" not in set(line):
            expanded.append(line)
            rows_empty_add.append(i)
        expanded.append(line)
    # get where to add columns
    col_empty_at = []
    for i in range(len(grid[0])):
        if all(line[i] == "." for line in grid):
            col_empty_at.append(i)

    # add columns
    for col in col_empty_at[::-1]:
        for row in range(len(expanded)):
            expanded[row] = expanded[row][:col] + "." + expanded[row][col:]

    return rows_empty_add, col_empty_at


def _get_galaxies(grid, rows_empty_add, col_empty_at, emptiness_factor=1) -> set[tuple[int, int]]:
    galaxies = set()
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == "#":
                expanded_y = y + sum(r < y for r in rows_empty_add) * emptiness_factor
                expanded_x = x + sum(c < x for c in col_empty_at) * emptiness_factor
                galaxies.add((expanded_y, expanded_x))
    return galaxies


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    rows_empty_add, col_empty_at = _expand_empty_space(input_data)

    all_galaxies = _get_galaxies(input_data, rows_empty_add, col_empty_at, emptiness_factor=1)

    compare = list(combinations(all_galaxies, 2))
    # calc distance
    distances = [sum([abs(g1[0] - g2[0]), abs(g1[1] - g2[1])]) for g1, g2 in compare]

    return sum(distances)


def part_2(input_file: str, emptiness_factor=1):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    rows_empty_add, col_empty_at = _expand_empty_space(input_data)

    all_galaxies = _get_galaxies(input_data, rows_empty_add, col_empty_at, emptiness_factor=emptiness_factor)

    compare = list(combinations(all_galaxies, 2))
    # calc distance
    distances = [sum([abs(g1[0] - g2[0]), abs(g1[1] - g2[1])]) for g1, g2 in compare]

    return sum(distances)


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 374

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt", emptiness_factor=10 - 1)
    print(result)
    assert result == 1030

    result = part_2("input_ex.txt", emptiness_factor=100 - 1)
    print(result)
    assert result == 8410

    result = part_2("input.txt", emptiness_factor=1_000_000 - 1)
    print(result)
