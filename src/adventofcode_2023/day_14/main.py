from pathlib import Path

from tqdm import tqdm


def count_load(grid) -> int:
    load = 0
    for y, line in enumerate(grid):
        for symbol in line:
            if symbol == "O":
                load += len(grid) - y

    return load


def tilt_grid(grid) -> list[str]:
    """Tilt grid north. All O will move as far north as they can or hit a #."""
    tilted_grid = ["" for _ in range(len(grid))]
    for x in range(len(grid[0])):
        count_round = 0
        block = -1
        for y in range(len(grid)):
            if grid[y][x] == "#":
                # move the current round_rocks to the block
                for i in range(count_round):
                    tilted_grid[block + i + 1] = tilted_grid[block + i + 1] + "O"
                # fill up with . up until current block
                for i in range(block + 1 + count_round, y):
                    tilted_grid[i] = tilted_grid[i] + "."
                # add the block #
                tilted_grid[y] = tilted_grid[y] + "#"
                block = y
                count_round = 0
            if grid[y][x] == "O":
                count_round += 1
        for i in range(count_round):
            tilted_grid[block + i + 1] = tilted_grid[block + i + 1] + "O"
        # fill up with . up until current block
        for i in range(block + 1 + count_round, len(grid)):
            tilted_grid[i] = tilted_grid[i] + "."

    return tilted_grid


def part_1(input_file: str, tilted_count=1):
    data_file = Path(__file__).with_name(input_file).read_text()
    grid = data_file.split("\n")

    tilted_grid = tilt_grid(grid)
    for _ in range(tilted_count - 1):
        # transpose the grid
        transposed = list(map(list, zip(*tilted_grid)))
        tilted_grid = ["".join(x) for x in transposed]

    return count_load(tilted_grid)


def part_2(input_file: str, tilted_count=1):
    data_file = Path(__file__).with_name(input_file).read_text()
    grid = data_file.split("\n")

    tilted_grid = tilt_grid(grid)
    for _ in tqdm(range(tilted_count - 1)):
        # transpose the grid
        # TODO gets transposed in the wrong direction
        transposed = list(map(list, zip(*tilted_grid)))
        tilted_grid = ["".join(x) for x in transposed]
        tilted_grid = tilt_grid(tilted_grid)

    return count_load(tilted_grid)


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 136

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)

    result = part_2("input_ex.txt", tilted_count=4)
    print(result)

    result = part_2("input_ex.txt", tilted_count=1000000000)
    print(result)
    assert result == 64

    result = part_2("input.txt", tilted_count=1000000000)
    print(result)
