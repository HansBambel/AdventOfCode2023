from pathlib import Path

from matplotlib import path


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    dig_path = [(0, 0)]
    for line in input_data:
        direction, distance, hexcode = line.split(" ")
        distance = int(distance)
        match direction:
            case "U":
                add_coord = (-1, 0)
            case "D":
                add_coord = (1, 0)
            case "L":
                add_coord = (0, -1)
            case "R":
                add_coord = (0, 1)
            case _:
                add_coord = (0, 0)

        dig_path.append((dig_path[-1][0] + distance * add_coord[0], dig_path[-1][1] + distance * add_coord[1]))

    min_y, max_y = min([coord[0] for coord in dig_path]), max([coord[0] for coord in dig_path])
    min_x, max_x = min([coord[1] for coord in dig_path]), max([coord[1] for coord in dig_path])
    whole_grid = [(x, y) for y in range(min_y, max_y + 1) for x in range(min_x, max_x + 1)]
    dig_path_grid = path.Path(dig_path)
    inner = dig_path_grid.contains_points(whole_grid)
    path_len = sum(
        [
            abs(dig_path[i][0] - dig_path[i + 1][0]) + abs(dig_path[i][1] - dig_path[i + 1][1])
            for i in range(len(dig_path) - 1)
        ]
    )

    return sum(inner) + path_len


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


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
    assert result == 1337

    result = part_2("input.txt")
    print(result)
