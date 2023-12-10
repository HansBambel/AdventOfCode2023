from pathlib import Path


def _find_start(grid) -> tuple[int, int]:
    for y, line in enumerate(grid):
        for x, val in enumerate(line):
            if val == "S":
                return y, x


def _get_connected_pipes(grid, y, x) -> list[tuple[int, int]]:
    connected_pipes = []

    match grid[y][x]:
        case "|":
            if y - 1 >= 0:
                connected_pipes.append((y - 1, x))
            if y + 1 < len(grid):
                connected_pipes.append((y + 1, x))
        case "-":
            if x - 1 >= 0:
                connected_pipes.append((y, x - 1))
            if x + 1 < len(grid[0]):
                connected_pipes.append((y, x + 1))
        case "L":
            if y - 1 >= 0:
                connected_pipes.append((y - 1, x))
            if x + 1 < len(grid[0]):
                connected_pipes.append((y, x + 1))
        case "J":
            if y - 1 >= 0:
                connected_pipes.append((y - 1, x))
            if x - 1 >= 0:
                connected_pipes.append((y, x - 1))
        case "7":
            if x - 1 >= 0:
                connected_pipes.append((y, x - 1))
            if y + 1 < len(grid):
                connected_pipes.append((y + 1, x))
        case "F":
            if x + 1 < len(grid[0]):
                connected_pipes.append((y, x + 1))
            if y + 1 < len(grid):
                connected_pipes.append((y + 1, x))
        case "S":
            # north
            if y - 1 >= 0 and grid[y - 1][x] in "|7F":
                connected_pipes.append((y - 1, x))
            # east
            if x + 1 < len(grid[0]) and grid[y][x + 1] in "-J7":
                connected_pipes.append((y, x + 1))
            # south
            if y + 1 < len(grid) and grid[y + 1][x] in "|LJ":
                connected_pipes.append((y + 1, x))
            # west
            if x - 1 >= 0 and grid[y][x - 1] in "-LF":
                connected_pipes.append((y, x - 1))

    if len(connected_pipes) > 2:
        print()
    return connected_pipes


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    grid = data_file.split("\n")

    start = _find_start(grid)

    visited = {start}
    current_pipes = [start]

    while len(current_pipes) > 0:
        current = current_pipes.pop()
        neighbors = _get_connected_pipes(grid, current[0], current[1])

        assert len(neighbors) <= 2
        for neighbor in neighbors:
            # Skip the one where we came from
            if neighbor in visited:
                continue
            current_pipes.append(neighbor)
            visited = visited.union((neighbor,))

    return len(visited) // 2


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 4

    result_ex = part_1("input_ex2.txt")
    print(result_ex)
    assert result_ex == 8

    result = part_1("input.txt")
    assert result < 8959
    assert result < 8958
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex3.txt")
    print(result)
    assert result == 4

    result_ex = part_1("input_ex4.txt")
    print(result_ex)
    assert result_ex == 8

    result_ex = part_1("input_ex5.txt")
    print(result_ex)
    assert result_ex == 10

    result = part_2("input.txt")
    print(result)
