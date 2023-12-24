from copy import copy
from pathlib import Path
from queue import Queue


def _path_to_state(path: list[tuple[int, int]]):
    return tuple((pos[0], pos[1]) for pos in path)


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    start = (0, 1)
    end = (len(input_data) - 1, len(input_data[0]) - 2)

    seen = set()
    Q = Queue()
    Q.put([start])
    longest_hike = 0
    while Q:
        path = Q.get()
        seen.add(_path_to_state(path))
        pos = path[-1]
        if pos == end:
            print("Found end with cost", len(path))
            longest_hike = max(longest_hike, len(path))
            continue
        for next_pos in [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]:
            if (
                next_pos[0] < 0
                or next_pos[1] < 0
                or next_pos[0] >= len(input_data)
                or next_pos[1] >= len(input_data[0])
            ):
                continue
            if next_pos in path:
                continue
            new_path = copy(path)
            new_path.append(next_pos)
            if _path_to_state(new_path) in seen:
                continue
            match input_data[next_pos[0]][next_pos[1]]:
                case "#":
                    continue
                case ".":
                    pass
                case "^":
                    next_pos = next_pos[0] - 1, next_pos[1]
                    new_path.append(next_pos)
                case "v":
                    next_pos = next_pos[0] + 1, next_pos[1]
                    new_path.append(next_pos)
                case "<":
                    next_pos = next_pos[0], next_pos[1] - 1
                    new_path.append(next_pos)
                case ">":
                    next_pos = next_pos[0], next_pos[1] + 1
                    new_path.append(next_pos)
            Q.put(new_path)
            print(Q.qsize())
    return longest_hike


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 94

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 1337

    result = part_2("input.txt")
    print(result)
