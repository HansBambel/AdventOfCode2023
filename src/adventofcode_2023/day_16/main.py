from functools import cache
from pathlib import Path
from typing import Literal

energized: set[tuple[int, int]] = set()
beams: set[tuple[int, int, Literal["^", ">", "v", "<"]]] = set()
grid: list[str] = ["unknown"]


@cache
def move_light(y: int, x: int, direction: Literal["^", ">", "v", "<"]):
    match direction:
        case "^":
            # check boundary
            if y - 1 < 0:
                return
            energized.add((y - 1, x))
            match grid[y - 1][x]:
                case "." | "|":
                    beams.add((y - 1, x, direction))
                case "-":
                    beams.add((y - 1, x, "<"))
                    beams.add((y - 1, x, ">"))
                case "/":
                    beams.add((y - 1, x, ">"))
                case "\\":
                    beams.add((y - 1, x, "<"))
        case ">":
            # check boundary
            if x + 1 >= len(grid[0]):
                return
            energized.add((y, x + 1))
            match grid[y][x + 1]:
                case "." | "-":
                    beams.add((y, x + 1, direction))
                case "|":
                    beams.add((y, x + 1, "^"))
                    beams.add((y, x + 1, "v"))
                case "/":
                    beams.add((y, x + 1, "^"))
                case "\\":
                    beams.add((y, x + 1, "v"))
        case "v":
            # check boundary
            if y + 1 >= len(grid):
                return
            energized.add((y + 1, x))
            match grid[y + 1][x]:
                case "." | "|":
                    beams.add((y + 1, x, direction))
                case "-":
                    beams.add((y + 1, x, ">"))
                    beams.add((y + 1, x, "<"))
                case "/":
                    beams.add((y + 1, x, "<"))
                case "\\":
                    beams.add((y + 1, x, ">"))
        case "<":
            # check boundary
            if x - 1 < 0:
                return
            energized.add((y, x - 1))
            match grid[y][x - 1]:
                case "." | "-":
                    beams.add((y, x - 1, direction))
                case "|":
                    beams.add((y, x - 1, "^"))
                    beams.add((y, x - 1, "v"))
                case "/":
                    beams.add((y, x - 1, "v"))
                case "\\":
                    beams.add((y, x - 1, "^"))


def get_start(y: int, x: int, direction: Literal["^", ">", "v", "<"]):
    global grid
    global beams

    if y == 0 and direction == "v":
        # beams start downwards
        match grid[y][x]:
            case "." | "|":
                beams.add((y, x, direction))
            case "-":
                beams.add((y, x, "<"))
                beams.add((y, x, ">"))
            case "/":
                beams.add((y, x, "<"))
            case "\\":
                beams.add((y, x, ">"))

    elif y == len(grid) - 1 and direction == "^":
        # beams start upwards
        match grid[y][x]:
            case "." | "|":
                beams.add((y, x, direction))
            case "-":
                beams.add((y, x, "<"))
                beams.add((y, x, ">"))
            case "/":
                beams.add((y, x, ">"))
            case "\\":
                beams.add((y, x, "<"))

    elif x == 0 and direction == ">":
        # beams start to the right
        match grid[y][x]:
            case "." | "-":
                beams.add((y, x, direction))
            case "|":
                beams.add((y, x, "^"))
                beams.add((y, x, "v"))
            case "/":
                beams.add((y, x, "^"))
            case "\\":
                beams.add((y, x, "v"))

    elif x == len(grid[0]) - 1 and direction == "<":
        # beams start to the left
        match grid[y][x]:
            case "." | "-":
                beams.add((y, x, direction))
            case "|":
                beams.add((y, x, "^"))
                beams.add((y, x, "v"))
            case "/":
                beams.add((y, x, "v"))
            case "\\":
                beams.add((y, x, "^"))


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    global grid
    global energized
    global beams

    grid = data_file.split("\n")
    energized = {(0, 0)}

    get_start(0, 0, ">")

    move_light.cache_clear()
    while len(beams) > 0:
        y, x, direction = beams.pop()
        move_light(y=y, x=x, direction=direction)

    return len(energized)


def trigger_beam_trace(y, x, direction):
    global beams

    get_start(y, x, direction)
    move_light.cache_clear()
    while len(beams) > 0:
        y, x, direction = beams.pop()
        move_light(y=y, x=x, direction=direction)


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    global grid
    global energized
    global beams

    grid = data_file.split("\n")

    max_energy = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            # skip the inner fields (we only start from the outside)
            if 0 < y < len(grid) - 1 and 0 < x < len(grid[0]) - 1:
                continue

            energized = {(y, x)}

            # when we are at corners go both directions
            if y == 0 and x == 0:
                trigger_beam_trace(y, x, ">")
                if len(energized) > max_energy:
                    max_energy = len(energized)
                energized = {(y, x)}
                trigger_beam_trace(y, x, "v")
            elif y == 0 and x == len(grid[0]) - 1:
                trigger_beam_trace(y, x, "<")
                if len(energized) > max_energy:
                    max_energy = len(energized)
                energized = {(y, x)}
                trigger_beam_trace(y, x, "v")
            elif y == len(grid) - 1 and x == 0:
                trigger_beam_trace(y, x, ">")
                if len(energized) > max_energy:
                    max_energy = len(energized)
                energized = {(y, x)}
                trigger_beam_trace(y, x, "^")
            elif y == len(grid) - 1 and x == len(grid[0]) - 1:
                trigger_beam_trace(y, x, "<")
                if len(energized) > max_energy:
                    max_energy = len(energized)
                energized = {(y, x)}
                trigger_beam_trace(y, x, "^")
            elif y == 0:
                trigger_beam_trace(y, x, "v")
            elif x == 0:
                trigger_beam_trace(y, x, ">")
            elif y == len(grid) - 1:
                trigger_beam_trace(y, x, "^")
            elif x == len(grid[0]) - 1:
                trigger_beam_trace(y, x, "<")

            if len(energized) > max_energy:
                max_energy = len(energized)

    return max_energy


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 46

    result = part_1("input.txt")
    assert result < 8406
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 51

    result = part_2("input.txt")
    print(result)
