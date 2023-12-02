import math
from pathlib import Path


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    valid_games = []
    max_balls = {"red": 12, "green": 13, "blue": 14}
    for line in input_data:
        valid = True
        game_id = int(line.split(": ")[0].split("Game ")[1])
        for sets in line.split(": ")[1].split("; "):
            for count_color in sets.split(", "):
                count, color = count_color.split(" ")
                if int(count) > max_balls[color]:
                    valid = False

        if valid:
            valid_games.append(game_id)

    return sum(valid_games)


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    total = []
    for line in input_data:
        min_balls = {"red": 0, "green": 0, "blue": 0}
        for sets in line.split(": ")[1].split("; "):
            for count_color in sets.split(", "):
                count, color = count_color.split(" ")
                if min_balls[color] < int(count):
                    min_balls[color] = int(count)

        total.append(math.prod(min_balls.values()))
    return sum(total)


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 8

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 2286

    result = part_2("input.txt")
    print(result)
