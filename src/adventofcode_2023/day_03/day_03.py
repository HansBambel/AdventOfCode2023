from pathlib import Path


def _in_boundary(grid: list[str], x: int, y: int) -> bool:
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return False
    return True


def _get_number_with_coords(grid: list[str], x: int, y: int) -> tuple[int, set[tuple[int, int]]]:
    # go to the left most index from the coords that is still a digit
    x_left, x_right = x, x
    number_coords = set()
    while _in_boundary(grid, x_left, y) and grid[y][x_left].isdigit():
        x_left -= 1
        number_coords.add((x_left, y))
    while _in_boundary(grid, x_right, y) and grid[y][x_right].isdigit():
        x_right += 1
        number_coords.add((x_right, y))
    found_number = grid[y][x_left + 1 : x_right]
    return int(found_number), number_coords


def _get_symbol_data(grid: list[str]) -> dict[tuple[int, int], str]:
    # go through input and find symbols that are not a digit or a "."
    # if we found one, check the neighbors for numbers
    symbols = {}
    for y, line in enumerate(grid):
        for x, symbol in enumerate(line):
            if symbol.isdigit() or symbol == ".":
                continue
            else:
                symbols[x, y] = symbol
    return symbols


def get_surrounding_part_numbers(input_data, x, y):
    symbol_part_numbers = []
    # check neighbors for numbers
    neighbors_to_check = {
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    }
    checked_surroundings = set()
    for check_x, check_y in neighbors_to_check:
        if not _in_boundary(input_data, check_x, check_y) or (check_x, check_y) in checked_surroundings:
            continue
        checked_surroundings.add((check_x, check_y))
        if input_data[check_y][check_x].isdigit():
            part_number, number_coords = _get_number_with_coords(input_data, check_x, check_y)
            symbol_part_numbers.append(part_number)
            # add those from number_coords to checked_surroundings that
            # also occur in neighbors_to_check using a set operation
            neighbors_checked = neighbors_to_check.intersection(number_coords)
            checked_surroundings = checked_surroundings.union(neighbors_checked)
    return symbol_part_numbers


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    symbols = _get_symbol_data(input_data)

    total = 0
    for (x, y), _ in symbols.items():
        symbol_part_numbers = get_surrounding_part_numbers(input_data, x, y)
        total += sum(symbol_part_numbers)
    return total


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    symbols = _get_symbol_data(input_data)
    total = 0
    for (x, y), symbol in symbols.items():
        if symbol != "*":
            continue
        symbol_part_numbers = get_surrounding_part_numbers(input_data, x, y)

        if len(symbol_part_numbers) == 2:
            total += symbol_part_numbers[0] * symbol_part_numbers[1]
    return total


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 4361

    result = part_1("input.txt")
    print(result)
    assert result > 330675

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 467835

    result = part_2("input.txt")
    print(result)
