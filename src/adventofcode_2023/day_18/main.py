from pathlib import Path

import numpy as np


def polygon_area(x, y):
    """Shoelace formula: https://stackoverflow.com/a/49129646/7132596"""
    correction = x[-1] * y[0] - y[-1] * x[0]
    main_area = np.dot(x[:-1], y[1:]) - np.dot(y[:-1], x[1:])
    return 0.5 * np.abs(main_area + correction)


def get_area_with_boundary(points: list[tuple[int, int]]) -> int:
    path_len = sum(
        [abs(points[i][0] - points[i + 1][0]) + abs(points[i][1] - points[i + 1][1]) for i in range(len(points) - 1)]
    )
    dig_arr = np.array(points)
    inner_area = polygon_area(dig_arr[:, 0], dig_arr[:, 1])
    return int(inner_area) + 1 + path_len // 2


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    dig_path = [(0, 0)]
    direction_map = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    for line in input_data:
        direction, distance, _ = line.split(" ")
        distance = int(distance)
        add_coord = direction_map[direction]
        last_loc = dig_path[-1]
        dig_path.append((last_loc[0] + distance * add_coord[0], last_loc[1] + distance * add_coord[1]))

    return get_area_with_boundary(dig_path)


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    dig_path = [(0, 0)]
    direction_map = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    dir_remap = {"0": "R", "1": "D", "2": "L", "3": "U"}
    for line in input_data:
        # convert the hexcode
        _, _, hexcode = line.split(" ")
        hexcode = hexcode[1:-1]
        distance = int(hexcode[1:-1], 16)
        direction = dir_remap[hexcode[-1]]

        distance = int(distance)
        add_coord = direction_map[direction]
        last_loc = dig_path[-1]
        dig_path.append((last_loc[0] + distance * add_coord[0], last_loc[1] + distance * add_coord[1]))

    return get_area_with_boundary(dig_path)


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 62

    result = part_1("input.txt")
    assert result > 35457
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 952408144115

    result = part_2("input.txt")
    print(result)
