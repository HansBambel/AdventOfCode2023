from pathlib import Path


def find_start(grid) -> tuple[int, int]:
    for y, row in enumerate(grid):
        if "S" in row:
            return y, row.index("S")


def part_1(input_file: str, max_steps=6):
    data_file = Path(__file__).with_name(input_file).read_text()
    grid = data_file.split("\n")
    possible_end_pos = set()
    start = find_start(grid)
    Q = [(start, 0)]
    seen = set()
    while Q:
        pos, steps = Q.pop(0)
        if (pos, steps) in seen:
            continue
        seen.add((pos, steps))
        if steps == max_steps:
            possible_end_pos.add(pos)
            continue
        y, x = pos
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= len(grid) or nx < 0 or nx >= len(grid[0]):
                continue
            if ((ny, nx), steps) not in seen and grid[ny][nx] != "#":
                Q.append(((ny, nx), steps + 1))
    return len(possible_end_pos)


def part_2(input_file: str, max_steps=6):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt", max_steps=6)
    print(result_ex)
    assert result_ex == 16

    result = part_1("input.txt", max_steps=64)
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt", 10)
    assert result == 50
    result = part_2("input_ex.txt", 50)
    assert result == 1594
    result = part_2("input_ex.txt", 100)
    assert result == 6536
    result = part_2("input_ex.txt", 500)
    assert result == 167004
    result = part_2("input_ex.txt", 1000)
    assert result == 668697
    result = part_2("input_ex.txt", 5000)
    assert result == 16733044

    result = part_2("input.txt", 26501365)
    print(result)
